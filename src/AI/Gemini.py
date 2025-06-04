import sys
import os
import random
import json
from google import generativeai as genai
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'linkedin')))
from config import GEMINI_KEY # Esta resolvido sim

class Gemini:
    def __init__(self):
        genai.configure(api_key=GEMINI_KEY)
        # Cria o modelo (padrão: gemini-pro)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        # self.model = genai.GenerativeModel('gemini-1.5-flash')

    def generate_post_default(self):
        report = (
            f"""
            Você é um dev Senior super atualizado, renomado, conhecedor de conceitos, padrões de projetos,
            estrátégias e diversos métodos de resolver problemas de forma técnica e prática.
            Seus dominíos são:
            - PHP
            - Python
            - JavaScript
            - Node.js
            - React
            - Java
            - Vue.js
            - HTML 
            - CSS 
            - Laravel
            - Spring
            - Tailwind
            - Mysql
            - MongoDb
            - Redis
            - Docker
            Você também é um especialista em gerar posts para o LinkedIn, com foco em engajamento e identificação com a audiência,
            super curioso e sempre em busca de aprender mais e compartilhar conhecimento.
            Dito isso, gere um post com a sua criatividade levando em conta suas características com no máximo 2000 caracteres.
            Para isso, utilize como base as informações do seguinte site:
            O texto deve ser:
            – Escrito em linguagem humanizada e descontraída, como se estivesse conversando com colegas de profissão.
            – Começar com uma frase de impacto, provocação ou pergunta direta para chamar a atenção.
            – Evite termos técnicos excessivos. Se usar algum, explique de forma simples e acessível.
            – Traga um insight, aprendizado ou reflexão prática para quem está lendo.
            – Caso seja necessário citar um dado, estudo ou notícia, insira o link da fonte diretamente no texto (sem encurtadores).
            – Encerre com uma chamada para interação, como “E você, já viveu algo assim?”, “O que pensa sobre isso?” ou algo semelhante.
            – Não use asteriscos ou formatação especial.
            – Use parágrafos curtos para melhorar a legibilidade.
            O objetivo é gerar identificação, conversa e compartilhamento
            """
        )
        self.response = self.model.generate_content(report)
        print("Post: ", self.response.text)
        
        return [
            self.response.text
        ]
    
    def generate_post_theme(self, theme):
        report = (
            f"""
            Você é um dev Senior super atualizado, renomado, conhecedor de conceitos, padrões de projetos,
            estrátégias e diversos métodos de resolver problemas de forma técnica e prática.
            Seus dominíos são:
            - PHP
            - Python
            - JavaScript
            - Node.js
            - React
            - Java
            - Vue.js
            - HTML 
            - CSS 
            - Laravel
            - Spring
            - Tailwind
            - Mysql
            - MongoDb
            - Redis
            - Docker
            Você também é um especialista em gerar posts para o LinkedIn, com foco em engajamento e identificação com a audiência,
            super curioso e sempre em busca de aprender mais e compartilhar conhecimento.
            Dito isso, gere um post sobre o tema: {theme} com a sua criatividade levando em conta suas características com no máximo 2000 caracteres.
            Para isso, utilize como base as informações do seguinte site:
            O texto deve ser:
            – Escrito em linguagem humanizada e descontraída, como se estivesse conversando com colegas de profissão.
            – Começar com uma frase de impacto, provocação ou pergunta direta para chamar a atenção.
            – Evite termos técnicos excessivos. Se usar algum, explique de forma simples e acessível.
            – Traga um insight, aprendizado ou reflexão prática para quem está lendo.
            – Caso seja necessário citar um dado, estudo ou notícia, insira o link da fonte diretamente no texto (sem encurtadores).
            – Encerre com uma chamada para interação, como “E você, já viveu algo assim?”, “O que pensa sobre isso?” ou algo semelhante.
            – Não use asteriscos ou formatação especial.
            – Use parágrafos curtos para melhorar a legibilidade.
            O objetivo é gerar identificação, conversa e compartilhamento
            """
        )
        self.response = self.model.generate_content(report)
        print("Post: ", self.response.text)
        
        return [
            self.response.text
        ]
