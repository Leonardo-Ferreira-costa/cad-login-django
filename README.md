# Cadastro Login

Sistema de autenticação e cadastro em Django com páginas separadas para cadastro, login, painel e home.

## Visão geral

Este projeto foi desenvolvido em Django e contém:

- Página inicial
- Cadastro de usuários
- Login de usuários
- Painel autenticado após login
- Logout
- Administração padrão do Django

## Estrutura do projeto

```text
cadastro-login/
├── app/
│   ├── templates/
│   │   └── app/
│   ├── views.py
│   └── ...
├── cadastro/
│   ├── templates/
│   │   └── cadastro/
│   ├── views.py
│   └── ...
├── login/
│   ├── templates/
│   │   └── login/
│   ├── views.py
│   └── ...
├── painel/
│   ├── templates/
│   │   └── painel/
│   ├── views.py
│   └── ...
├── sistema/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── db.sqlite3
├── manage.py
├── env/
├── README.md
└── requirements.txt (se adicionado posteriormente)
```

## Tecnologias

- Python
- Django 6.1
- SQLite
- HTML

## Pré-requisitos

- Python 3.10 ou superior
- Ambiente virtual recomendado
- Git (opcional)

## Como executar

1. Acesse a pasta do projeto:

```bash
cd cadastro-login
```

2. Ative o ambiente virtual:

No Windows:

```bash
env\Scripts\activate
```

3. Execute as migrações do banco de dados:

```bash
python manage.py migrate
```

4. Inicie o servidor local:

```bash
python manage.py runserver
```

5. Abra no navegador:

```text
http://127.0.0.1:8000/
```

## Rotas principais

- `/` — página inicial
- `/cadastro/` — cadastro de usuário
- `/login/` — login
- `/painel/` — painel principal (requer autenticação)
- `/logout/` — encerra a sessão do usuário
- `/admin/` — área administrativa do Django

## Funcionalidades

- Registro de novos usuários
- Validação de confirmação de senha
- Verificação de usuário duplicado
- Login com autenticação do Django
- Redirecionamento para painel após login
- Proteção de acesso com `@login_required`

## Observações

- A senha do usuário é criada com `create_user`, que gera a hash corretamente.
- O banco usado é o SQLite, armazenado em `db.sqlite3`.
- O projeto está em modo de desenvolvimento (`DEBUG = True`).

## Criar usuário administrador

Para acessar a área administrativa do Django:

```bash
python manage.py createsuperuser
```

Depois, acesse:

```text
http://127.0.0.1:8000/admin/
```

## Licença

Este projeto foi desenvolvido para fins de estudo e prática de Django.
