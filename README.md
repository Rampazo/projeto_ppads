# Projeto PPADS

Este projeto tem como objetivo oferecer uma rede social de recomendações de livros, filmes e séries.

## Ferramentas

- python 3.8

## Instalação

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python3 app/__main__.py
```

## Rotas

- ### Frontend
  - /login -> Tela de Login
  - /user/registration -> Tela de registro de usuário
  - /feed -> Tela de Feed

- ### Backend
  - POST /login/auth -> Valida autenticação
  - POST /user/create -> Cria usuário