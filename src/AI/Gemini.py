import sys
import os
import random
import json
from google import generativeai as genai
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'linkedin')))
from config import GEMINI_KEY # Esta resolvido sim

sites = [
    'https://www.techradar.com/',                # Notícias e tendências em tecnologia
    'https://www.medium.com/',                  # Artigos de desenvolvedores e especialistas
    'https://www.stackoverflow.com/',           # Discussões técnicas e soluções de problemas
    'https://www.github.com/',                  # Repositórios de código e tendências de frameworks
    'https://www.hackernews.com/',              # Notícias e tendências em tecnologia
    'https://www.dev.to/',                      # Plataforma de conteúdo para desenvolvedores
    'https://www.smashingmagazine.com/',        # Design web, UX/UI e desenvolvimento front-end
    'https://www.digitalocean.com/community/',  # Artigos sobre DevOps, Cloud e desenvolvimento
    'https://www.redhat.com/en/blog',           # Blogs sobre Linux, DevOps e computação em nuvem
    'https://www.turing.com/blog/',             # Artigos sobre IA, Machine Learning e desenvolvimento
    'https://www.infoq.com/',                  # Artigos sobre arquitetura de software e metodologias ágeis
    'https://www.docker.com/blog/',             # Conteúdo sobre containers e orquestração
    'https://www.theverge.com/tech',            # Notícias de tecnologia, incluindo inovações e tendências
    'https://www.arxiv.org/',                   # Publicações acadêmicas sobre computação e IA
    'https://www.cio.com/',                     # Tendências de tecnologia em empresas
    'https://www.researchgate.net/',            # Artigos acadêmicos e pesquisas em tecnologia
    'https://www.coursera.org/',                # Cursos sobre tecnologias emergentes
    'https://www.edx.org/',                     # Cursos e materiais sobre desenvolvimento técnico
    'https://www.codeproject.com/',             # Artigos, tutoriais e fóruns para desenvolvedores
    'https://www.zdnet.com/',                   # Notícias e análises sobre tecnologia e software
    'https://www.eweek.com/',                   # Notícias de TI e tendências em desenvolvimento
    'https://www.linkedin.com/learning/',       # Cursos e artigos sobre habilidades técnicas
    'https://www.wired.com/category/tech/',      # Notícias e análises de tecnologia e inovação
    'https://www.technologyreview.com/',        # Inovações tecnológicas e tendências futuras
    'https://www.venturebeat.com/',             # Notícias sobre startups e tecnologias emergentes
    'https://www.oreilly.com/',                 # Conteúdo sobre livros, tutoriais e cursos em tecnologia
    'https://www.mashable.com/tech',            # Notícias sobre inovações em tecnologia
]

temas = [
    'Tendências de IA e Machine Learning em 2025',
    'Como otimizar a performance de APIs RESTful',
    'Melhores práticas para desenvolvimento com microserviços',
    'Automação de testes com Selenium e Cypress',
    'Principais ferramentas para monitoramento de aplicações em produção',
    'Como integrar aplicações com GraphQL',
    'Design Patterns mais usados no desenvolvimento de software',
    'Desenvolvimento ágil: Scrum vs Kanban, qual a melhor abordagem?',
    'A importância de DevOps na entrega contínua',
    'Trabalhando com Docker e Kubernetes no desenvolvimento de software',
    'Introdução à arquitetura serverless e suas vantagens',
    'Como aplicar segurança em aplicações com OAuth e JWT',
    'Integração de sistemas com RabbitMQ e Kafka',
    'A evolução dos frameworks JavaScript: React, Vue e Angular',
    'Como usar testes unitários no PHP com PHPUnit',
    'Gerenciamento de banco de dados com MongoDB e MySQL',
    'Práticas para garantir a escalabilidade de sistemas',
    'Blockchain e suas aplicações no desenvolvimento de sistemas',
    'Como utilizar CI/CD para automação de pipelines',
    'A importância do versionamento de código com Git',
    'Frameworks para criação de APIs: Laravel, Express, Django',
    'Gestão de projetos e como escolher a metodologia certa',
    'O impacto da computação em nuvem no desenvolvimento de software',
    'Desenvolvimento seguro: Boas práticas para evitar vulnerabilidades',
    'Como gerenciar dependências e pacotes em projetos de software',
    'A ascensão da computação quântica no desenvolvimento de sistemas',
    'Transformação digital: Como a tecnologia está mudando os negócios',
    'O papel dos containers e orquestração no desenvolvimento moderno',
    'Como garantir a privacidade de dados no desenvolvimento de software',
    'Melhorando a experiência do usuário com design responsivo',
    'Técnicas para otimização de banco de dados e consulta de dados',
    'Comportamento ético no desenvolvimento de software',
    'A importância da documentação no desenvolvimento de software',
    'Como lidar com a dívida técnica em projetos de software',
    'A evolução das linguagens de programação: do Assembly ao Python',
    'Como aplicar princípios SOLID no desenvolvimento de software',
    'A importância do feedback contínuo no desenvolvimento ágil',
]
class Gemini:
    def __init__(self):
        genai.configure(api_key=GEMINI_KEY)
        # Cria o modelo (padrão: gemini-pro)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        # self.model = genai.GenerativeModel('gemini-1.5-flash')

    def generate_post(self, option):

        ## SITES
        if option == '1':
            conteudo_index = random.randint(0, len(sites) - 1)
            site = sites[conteudo_index]

            print("Conteudo: ", site)
            report = (
                f"""
                Gere um post para o LinkedIn com no máximo 2000 caracteres. Com o tema que você achar pertinente dentro do site.
                Para isso, utilize como base as informações do seguinte site: {site}.
                O texto deve ser:
                – Escrito em linguagem humanizada e descontraída, como se estivesse conversando com colegas de profissão.
                – Começar com uma frase de impacto, provocação ou pergunta direta para chamar a atenção.
                – Evite termos técnicos excessivos. Se usar algum, explique de forma simples e acessível.
                – Conte uma breve história ou experiência real relacionada ao tema (se fizer sentido).
                – Traga um insight, aprendizado ou reflexão prática para quem está lendo.
                – Caso use alguma informação extraída do site, cite claramente o link da fonte dentro do texto (sem encurtadores).
                – Encerre com uma chamada para interação, como “E você, já viveu algo assim?”, “O que pensa sobre isso?” ou algo semelhante.
                – Não use asteriscos, emojis ou formatação especial.
                – Use parágrafos curtos para melhorar a legibilidade.

                O objetivo é gerar identificação, conversa e compartilhamento
                """
            )
            self.response = self.model.generate_content(report)
            print("Post: ", self.response.text)
        

        ## CONTEUDOS
        if option == '2':
            conteudo_index = random.randint(0, len(temas) - 1)
            tema = temas[conteudo_index]

            print("Conteudo: ", tema)
            report = (
                f"""
                Gere um post para o LinkedIn com no máximo 2000 caracteres. O tema é: {tema}.
                O texto deve ser:
                – Escrito em linguagem humanizada e descontraída, como se estivesse conversando com colegas de profissão.
                – Engajador desde a primeira linha (com uma frase de impacto, provocação ou pergunta direta).
                – Evite termos técnicos excessivos e, se usar, explique de forma simples.
                – Inclua uma breve história ou experiência pessoal relacionada ao tema (se fizer sentido).
                – Traga um insight, aprendizado ou reflexão útil e prática para quem está lendo.
                – Termine com uma pergunta ou chamada para interação nos comentários, como: “E você, já passou por isso?”, “O que você pensa sobre isso?”, etc.
                – Caso seja necessário citar um dado, estudo ou notícia, insira o link da fonte diretamente no texto (sem encurtadores).
                – Não use asteriscos, emojis ou formatações especiais.
                – Estruture o texto com quebras de parágrafo para facilitar a leitura.

                O objetivo é gerar identificação, conversa e compartilhamento
                """
            )
            self.response = self.model.generate_content(report)
            print("Post: ", self.response.text)

        prompt = (
            f"""
            Gere um prompt para criar uma imagem com base nesse post: {self.response.text}, com no máximo 512 caracteres. Caso seja um conceito técnico, me de um prompt para criar um diagrama
            """
        )
        self.prompt_img = self.model.generate_content(prompt)

        print("Prompt: ", self.prompt_img.text)

        return [
            self.response.text,
            self.prompt_img.text,
        ]
