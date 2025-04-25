from src.linkedin.config import CLIENT_ID, REDIRECT_URI_URL_ENCODED, CLIENT_SECRET

import requests

class Auth:
    def exchange_code_for_a_token(self, code):
        url = "https://www.linkedin.com/oauth/v2/accessToken"

        payload = f'grant_type=authorization_code&code={code}&redirect_uri={REDIRECT_URI_URL_ENCODED}&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}%3D%3D'
        headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '__cf_bm=OS1Pynf29ZZjx61vswF9IWuPIGK2UHjUFmuoUHTdlms-1745594817-1.0.1.1-12Drqr8efqUy6By0AvAqKcrBholaZBlSofc7EdlPrOhntD0qiFRW5YQgfSiNDIbXEmLRLyeGVDZIVanB9HVpHaZgVe.TWZpLdE48MBP0kkI; bcookie="v=2&1457db9b-e453-4f57-8f58-92d1f7b9e4db"; lang=v=2&lang=en-us; lidc="b=VB99:s=V:r=V:a=V:p=V:g=3429:u=499:x=1:i=1745595122:t=1745679241:v=2:sig=AQEeaBcvk9qiwO3-y7aibb51p620DfFG"; bscookie="v=1&2025042315352217795252-1520-4608-8226-bb654ff6cf68AQFFQFyapOODqHz8tMU49xqUCV9rY80G"'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print("Status da resposta", response.status_code)
        if response.status_code != 200:
            print("Erro na requisição para troca de code por token", response.json())
            return False
        
        print("Sucesso na requisição para troca de code por token", response.json())
        access_token = response.json().get('access_token')
        print('Access Token:', access_token)
        return access_token