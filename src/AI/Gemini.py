import sys
import os

# Pega o caminho absoluto da pasta atual, volta uma pasta e entra na outra
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'linkedin')))

from config import GEMINI_KEY # Esta resolvido sim
from google import generativeai as genai

# Configure sua API Key
genai.configure(api_key=GEMINI_KEY)

# Cria o modelo (padrão: gemini-pro)
model = genai.GenerativeModel('gemini-2.0-flash')

# Faz uma pergunta
pergunta = "Explique de maneira simples o que é Machine Learning."
response = model.generate_content(
    pergunta
)

# Mostra a resposta
print("Resposta da IA:")
print(response.text)
