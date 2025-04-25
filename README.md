# 🤖 Publicador Automático no LinkedIn com IA

Este projeto permite publicar automaticamente conteúdos no LinkedIn utilizando a API oficial da plataforma. Ele integra funcionalidades de geração de conteúdo com IA (como GPT) e realiza o processo de autenticação, envio e monitoramento de posts de forma programada e segura.

---

## 🚀 Funcionalidades

- ✅ Autenticação com a API do LinkedIn via OAuth 2.0
- 🧠 Geração de texto dinâmico com IA (ex: OpenAI)
- 🖼️ Publicação de posts com ou sem mídia (imagem, vídeo)
- 📅 Agendamento de publicações (opcional)
- 📥 Armazenamento e gerenciamento do token de acesso via SQLite
- 🔄 Atualização automática do token e validade

---

## 🧰 Tecnologias Utilizadas

- **Python 3.10+**
- **Requests** – para comunicação com a API do LinkedIn
- **SQLite3** – para armazenar `access_token` e data de validade
- **OpenAI** (ou outra IA) – para geração de conteúdo opcional
- **Ngrok** (ou similar) – para testes locais com callback da OAuth

---

## 🗂️ Estrutura Básica

