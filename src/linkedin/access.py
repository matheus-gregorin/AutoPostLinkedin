from src.linkedin.config import CLIENT_ID, REDIRECT_URI
from urllib.parse import urlencode
import webbrowser


class Access:
    def recovery_code(self):
        scope = 'openid profile email w_member_social'

        auth_url = 'https://www.linkedin.com/oauth/v2/authorization?' + urlencode({
            'response_type': 'code',
            'client_id': CLIENT_ID,
            'redirect_uri': REDIRECT_URI,
            # 'state': '', # Caso queira que retorne um estado específico
            'scope': scope
        })

        # Abre o navegador para você fazer login
        webbrowser.open(auth_url)
