import requests

TEXT = "Texto principal"

MEDIA_CATEGORY = [
    "NONE",
    "IMAGE",
    "VIDEO",
    "ARTICLE"
]

MEDIA_UR = "URN da MIDIA que subimos"

class Publish:
    def post_publish(self, access_token, urn, text, media_category, media_urn):
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
            'X-Restli-Protocol-Version': '2.0.0',
            'LinkedIn-Versuion': '202308',
        }

        post_data = {
            "author": f"urn:li:person:{urn}",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {},
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }

        # Valida e adiciona texto
        if text:
            post_data["specificContent"]["com.linkedin.ugc.ShareContent"]["shareCommentary"]["text"] = text

        # Valida e adiciona categoria de mídia
        if media_category:
            post_data["specificContent"]["com.linkedin.ugc.ShareContent"]["shareMediaCategory"] = media_category

        # Valida e adiciona mídia (caso seja imagem, vídeo etc)
        if media_urn:
            post_data["specificContent"]["com.linkedin.ugc.ShareContent"]["media"] = [
                {
                    "status": "READY",
                    "description": { 
                        "text": "Imagem via API" 
                    },
                    "media": media_urn,
                    "title": { 
                        "text": "Img" 
                    }
                }
            ]

        response = requests.post('https://api.linkedin.com/v2/ugcPosts', headers=headers, json=post_data)

        print("Status da resposta", response.status_code)
        if response.status_code != 201:
            print("Erro na requisição para publicar post", response.json())
            return False
        
        print("Sucesso na requisição para publicar post", response.json())
        id = response.json().get('id')
        print('ID da requisição:', access_token)
        return id
