import sys
sys.dont_write_bytecode = True
import time
from datetime import date
from dateutil.relativedelta import relativedelta
from datetime import datetime
from src.linkedin.config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from src.db.database import TokenManager
from src.linkedin.access import Access
from src.linkedin.auth import Auth
from src.linkedin.get_urn import CollectUrn
from src.linkedin.post import Publish
from src.AI.Gemini import Gemini

class MainLoop:
    def __init__(self):
        # Class
        self.access = Access()
        self.auth = Auth()
        self.get_user_info = CollectUrn()
        self.post = Publish()
        self.ia = Gemini()

        # Variáveis
        self.client_id = CLIENT_ID
        self.client_secret = CLIENT_SECRET
        self.redirect_uri = REDIRECT_URI
        self.sub = ''

        self.manager = TokenManager('src/db/database.db')

        self.code = self.manager.obter_token('code')
        self.access_token = self.manager.obter_token('access')
        self.date_validate = self.manager.obter_validade('code')

    def run(self):

        self.running = True
        while self.running:

            print("Iniciando...")
            time.sleep(3)

            option = input("Digite para mim a opção desejada: \n1 - Gerar post de site\n2 - Post sobre um tema\n3 - Sair\n")
            
            post = []
            if option == '1':
                print("Gerando post de site...")
                post = self.ia.generate_post_default()
            
            if option == '2':
                print("Gerando post sobre um tema...")
                theme = input("Digite o tema do post: ")
                post = self.ia.generate_post_theme(theme)
        
            if option == '3':
                print("Saindo...")
                self.running = False
                return

            # Aguardando 3 segundos para simular processamento
            time.sleep(3)

            # Gerar post com IA
            print("Post gerado com IA: ", post)
            time.sleep(3)

            print("Validando code do Linkedin...")
            time.sleep(3)

            is_valid = self.valid_date()
            time.sleep(3)

            # Se o código se tornar inválido, gere um novo
            if not is_valid:
                self.revalidating_code()

            print("Coletando URN do usuario...")
            time.sleep(3)

            sub = self.get_user_info.get_urn(self.access_token)
            time.sleep(3)

            if not sub:
                print("Erro ao obter sub")
                self.running = False
                return

            print("Publicando POST...")
            time.sleep(3)

            id = self.post.post_publish(self.access_token, sub, " ".join(post), "NONE", "DRAFT", "")
            time.sleep(3)

            if not id:
                print("Erro ao postar")
                self.running = False
                return

            self.running = False


    def revalidating_code(self):

        self.access.recovery_code() # Abrindo no browser a pagina para recuperar o código
        self.code = input("Digite o código aqui: ") # Pegue o código na URL após a autenticação
        print("Codigo atualizado: ", self.code)
        self.manager.atualizar_token('code', self.code)

        # Data atual + 2 meses
        data_futura = date.today() + relativedelta(months=2)
        # Formatar como 'YYYY-MM-DD'
        data_formatada = data_futura.strftime('%Y-%m-%d')

        self.manager.atualizar_validade('code', data_formatada)
        self.date_validate = data_formatada
        time.sleep(3)
        
        print("Trocando code por um access_token")
        time.sleep(3)

        # Se o código for válido, trocar o code por um token
        token = self.auth.exchange_code_for_a_token(self.code)
        time.sleep(3)

        if not token:
            print("Erro ao obter token")
            self.running = False
            return

        print("Sucesso ao trocar code por token")
        self.access_token = token
        print("Token atualizado: ", self.access_token)
        self.manager.atualizar_token('access', self.access_token)
        self.manager.atualizar_validade('access', data_formatada)
        time.sleep(3)

    def valid_date(self):

        print("Data de validade: ", self.date_validate)

        validation_date = datetime.strptime(self.date_validate, '%Y-%m-%d').date()
        date_current = datetime.now().date()
        print("Data atual:", date_current, "Valido até:", validation_date)

        # Data de vencimento é inferior a data atual?
        if validation_date >= date_current:
            print("Código continua válido")
            return True
        else:
            print("Código inválido, necessário gerar um novo código")
            return False

if __name__ == "__main__":
    main = MainLoop()
    main.run()
