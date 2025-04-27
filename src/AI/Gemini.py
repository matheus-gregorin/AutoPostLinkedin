import sys
import os
import random
import json
from google import generativeai as genai
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'linkedin')))
from config import GEMINI_KEY # Esta resolvido sim

# COLOCAR EM UM ARRAY OS SITES QUE DESEJA SCANNEAR
sites = [
    "https://dev.to/",
    "https://canaltech.com.br/"
]
class Gemini:
    def __init__(self):
        genai.configure(api_key=GEMINI_KEY)
        # Cria o modelo (padrão: gemini-pro)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        # self.model = genai.GenerativeModel('gemini-1.5-flash')

    def ask_question(self):
        site_index = random.randint(0, len(sites) - 1)
        site = sites[site_index]  # Agora pegamos o site certo!
        
        report = (
            f"""
            Gere um post para o linkedin de desenvolvimento de sistemas com base em conceitos consolidados, de forma descontraida, aprofundada e que chame a atenção com alguma chamada no inicio do texto(se precisar de links na publicação, insira você mesmo). Com no máximo 3000 caracteres.
            """
        )
        self.response = self.model.generate_content(report)

        prompt = (
            f"""
            Gere um prompt para criar uma imagem com base nesse post: {self.response.text}, com no máximo 512 caracteres: {site}.
            """
        )
        self.prompt_img = self.model.generate_content(prompt)

        return [
            self.response.text,
            self.prompt_img.text,
        ]
