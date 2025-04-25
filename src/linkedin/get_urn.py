import requests

class CollectUrn:
    def get_urn(self, access_token):
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
            'X-Restli-Protocol-Version': '2.0.0',
            'LinkedIn-Versuion': '202308',
        }

        # Primeiro, pegar seu URN (identificador de perfil)
        profile = requests.get('https://api.linkedin.com/v2/userinfo', headers=headers)

        print("Status da resposta", profile.status_code)
        if profile.status_code != 200:
            print("Erro na requisição para pegar URN (SUB) do user: ", profile.json())
            return False

        print("Sucesso na requisição para pegar URN (SUB) do user", profile.json())
        urn = profile.json().get('sub') # EQUIVALENTE AO URN
        print('URN:', urn)
        return urn