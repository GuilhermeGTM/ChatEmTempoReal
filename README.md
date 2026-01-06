#  💬 Projeto Chat em Tempo Real com Django Channels

# 📌 Sobre o Projeto
O objetivo é criar um ambiente de comunicação simples e eficiente, onde cada sala de chat possui autenticação e os usuários podem interagir em tempo real.  
O sistema foi desenvolvido para fins de aprendizado e pode ser expandido para aplicações maiores.

---
  

## Layout web
![Web 1](https://github.com/GuilhermeGTM/ChatEmTempoReal/blob/main/image_git/1.png)

![Web 1](https://github.com/GuilhermeGTM/ChatEmTempoReal/blob/main/image_git/3.png)


---

# ⚙️ Tecnologias utilizadas
- **Backend:** Django 4+, Django Channels
- **Tempo real:** WebSockets, Channel Layer (Redis)
- **Frontend:** HTML, JavaScript (ES6), Bootstrap 5
- **Servidor ASGI:** Daphne
- **Linguagem:** Python 3.10+
- **Banco de dados:** SQLite (dev) ou PostgreSQL (prod)
- **Ambiente:** Virtualenv, pip
- **Estilo e utilitários:** CSS via Bootstrap, Flexbox util classes

---

## DB
- SQLite3

---

# 🚀 Funcionalidades

| Funcionalidade                  | Descrição                                                                 |
|---------------------------------|---------------------------------------------------------------------------|
| Criação e autenticação de salas | Usuários só entram em salas existentes mediante nome e senha.             |
| Identificação por apelido        | Cada usuário escolhe um apelido que aparece junto às mensagens.           |
| Envio de mensagens em tempo real | Comunicação instantânea via WebSockets com Django Channels.               |
| Interface responsiva             | Layout centralizado e estilizado com Bootstrap, adaptável a desktop e mobile. |
| Envio pelo botão ou tecla Enter  | Mensagens podem ser enviadas clicando em "Enviar" ou pressionando Enter.  |


---

# Como executar o projeto

```bash
instalar o venv na pasta do projeto
--->python -m venv .venv
ativando venv
--->.\.venv\Scripts\Activate
baixando as dependencias
--->python -m pip install -r requirements.txt
--->python manage.py migrate
-->python manage.py runserver
Configurar as chaves no settings
```

---

# Autor

Guilherme Timm Moreira

