# Sistema de Cadastro e Login com Ativação por E-mail

Projeto desenvolvido em Django para gerenciar cadastro, ativação de conta por e-mail e login com autenticação em duas etapas (MFA).

## Visão geral

Este sistema permite:

- cadastro de novos usuários
- confirmação de senha
- validação de e-mail único
- ativação da conta através de link enviado por e-mail
- login apenas para usuários ativos
- autenticação em duas etapas com código enviado por e-mail
- expiração do código MFA após 5 minutos
- uso único dos códigos MFA
- painel autenticado após login
- logout e administração padrão do Django

## Funcionalidades implementadas

- Cadastro com nome de usuário informado pelo usuário
- Armazenamento do nome visual do usuário em `first_name`
- Usuário interno do Django com `username` gerado automaticamente para evitar duplicidade
- Validação focada no `email`, em vez de nome de usuário
- Bloqueio de cadastro caso o e-mail já exista
- Criação do usuário com `is_active=False`
- Envio de e-mail com link de ativação
- Ativação da conta ao acessarem o link gerado
- Redirecionamento para a tela de login após ativação
- Geração e envio de código MFA após a senha ser validada
- Invalidação de códigos MFA anteriores quando um novo código é gerado
- Conclusão do login somente após a confirmação do código MFA

## Fluxo de cadastro e ativação

1. O usuário preenche cadastro com nome, e-mail e senha.
2. O sistema valida:
   - senha e confirmação iguais
   - senha com pelo menos 8 caracteres
   - e-mail ainda não cadastrado
3. O usuário é criado como inativo.
4. Um link de ativação é gerado e enviado por e-mail.
5. Ao clicar no link, o sistema ativa o usuário.
6. O usuário informa o e-mail e a senha na tela de login.
7. O sistema envia um código MFA de seis dígitos por e-mail.
8. O usuário informa o código na segunda etapa e acessa o painel.

## Fluxo de autenticação em duas etapas

1. O sistema localiza o usuário pelo e-mail informado.
2. A senha é validada usando o sistema de autenticação padrão do Django.
3. Códigos MFA anteriores e ainda não usados são invalidados.
4. Um novo código de seis dígitos é salvo no banco e enviado por e-mail.
5. O ID do usuário fica temporariamente armazenado na sessão.
6. O código é aceito somente se não tiver sido usado e ainda estiver dentro do prazo de 5 minutos.
7. Após a validação, o código é marcado como usado, a sessão é autenticada e o usuário é redirecionado para o painel.

## Estrutura do projeto

```text
cadastro-login/
├── app/
│   ├── templates/
│   │   └── app/
│   └── views.py
├── cadastro/
│   ├── templates/
│   │   └── cadastro/
│   └── views.py
├── login/
│   ├── templates/
│   │   └── login/
│   │       ├── login.html
│   │       └── mfa.html
│   ├── models.py           # Modelo TwoFactorCode
│   └── views.py
├── painel/
│   ├── templates/
│   │   └── painel/
│   └── views.py
├── sistema/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── env/
├── requirements.txt
├── README.md
└── .gitignore
```

## Tecnologias

- Python
- Django 6.1
- SQLite
- HTML
- SMTP para envio de e-mails

## Pré-requisitos

- Python 3.10 ou superior
- Ambiente virtual
- Git opcional

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

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute as migrações:

```bash
python manage.py migrate
```

5. Inicie o servidor:

```bash
python manage.py runserver
```

6. Acesse no navegador:

```text
http://127.0.0.1:8000/
```

## Rotas principais

- `/` — página inicial
- `/cadastro/` — cadastro de usuário
- `/login/` — login
- `/painel/` — painel principal (requer autenticação)
- `/logout/` — encerra a sessão
- `/ativar/<uidb64>/<token>/` — ativação da conta
- `/admin/` — painel administrativo do Django

## Configuração de e-mail

A aplicação usa o backend SMTP do Django para enviar o link de ativação e o código MFA. O arquivo `sistema/settings.py` contém as configurações do e-mail, incluindo:

- `EMAIL_BACKEND`
- `EMAIL_HOST`
- `EMAIL_PORT`
- `EMAIL_USE_TLS`
- `EMAIL_HOST_USER`
- `EMAIL_HOST_PASSWORD`
- `DEFAULT_FROM_EMAIL`

Para funcionar corretamente, informe as credenciais do serviço de e-mail no arquivo de configuração antes de testar o cadastro.

O e-mail do código MFA usa atualmente o remetente `no-reply@difusao.tech`, definido em `login/views.py`. Em produção, esse remetente deve ser alinhado ao serviço SMTP configurado em `settings.py`.

Exemplo de configuração:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'seu-email@gmail.com'
EMAIL_HOST_PASSWORD = 'sua-senha-ou-app-password'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```

> Em ambiente de desenvolvimento, também é possível usar o backend de console para visualizar os e-mails no terminal, mas a implementação atual está configurada para SMTP.

## Observações importantes

- O campo `username` do Django é gerado automaticamente e não é mostrado ao usuário final.
- O nome real do usuário é salvo em `first_name`.
- A verificação de usuário duplicado é feita pelo `email`.
- Usuários que ainda não ativaram a conta não podem fazer login.
- O código MFA expira após 5 minutos e não pode ser reutilizado.
- É necessário configurar o SMTP para testar o envio do link de ativação e do código MFA.

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

Este projeto foi desenvolvido para fins de estudo e prática com Django.
