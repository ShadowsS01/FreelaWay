# FreelaWay

[![licence mit](https://img.shields.io/badge/licence-MIT-blue)](LICENSE)

> Um projeto usando o Framework Django para desenvolver uma aplicação web.

## Tecnologias utilizadas

- Frontend:
  - [Tailwind CSS](https://tailwindcss.com/) - Uma estrutura CSS de utilidade para o desenvolvimento rápido de interface do usuário.
  - [Bootstrap](https://getbootstrap.com/) - A estrutura HTML, CSS e JavaScript mais popular para desenvolver projetos responsivos e mobile first na web.
- Backend:
  - [Python](https://www.python.org/) - Python é uma linguagem de programação que permite trabalhar rapidamente e integrar os sistemas de forma mais eficaz.
  - [Django](https://www.djangoproject.com/) - Django é um framework web Python de alto nível que encoraja o desenvolvimento rápido e design limpo e pragmático.

## Demo

[https://freelawayh.herokuapp.com/jobs/encontrar_jobs/](https://freelawayh.herokuapp.com/jobs/encontrar_jobs/)

## Como executar o projeto

Para executar o projeto você precisa ter o [Python](https://www.python.org/) e o [Git](https://git-scm.com) instalados na sua maquina. Você também precisará de um editor de código, eu utilizei o [VSCode](https://code.visualstudio.com).

### 1. Clone esse repositório

```bash
git clone https://github.com/ShadowsS01/FreelaWay.git
```

### 2. Acesse a pasta do projeto

```bash
cd FreelaWay
```

### 3. Ambiente virtual

Inicie um ambiente virtual e ative-o. Se não souber como, isso pode ajudar: (<https://docs.python.org/pt-br/3/tutorial/venv.html>).

### 4. instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Configurar variáveis de ambiente

Copie o arquivo `.env.example` neste diretório para `.env` (que será ignorado pelo Git):

```bash
cp .env.example .env
```

- Se der errado o `cp` crie o arquivo `.env` nesta pasta.

Em seguida, defina cada variável em `.env`:

```text
SECRET_KEY=Digite_Uma_Senha_Secreta_aqui
DEBUG=True
```

- Antes de ir para a proxima etapa, é necessário fazer uma alteração no `settings.py` na pasta do projeto `freelaway`.
- Entre na pasta do projeto, vá até o final do arquivo `settings.py`, comente ou remova as linhas da AWS. Estas são as últimas linhas após o comentário `#AWS`

### 7. Migações no Banco Dados

Agora precisamos fazer as migrações para o banco de dados, só rodar no terminal:

```bash
python manage.py migrate
```

### 8. Criando o Super Usuário

- Ele vai pedir algumas informações do tipo usuário, e-mail e senha.
- Digite o que desejar, recomendo só digitar um usuário e uma senha que se lembre, só para conseguir acessar a área administrativa.

```bash
python manage.py createsuperuser
```

### 9. Executando aplicação em modo de desenvolvimento

```bash
python manage.py runserver
```

- A aplicação inciará localmente - acesse: (<http://127.0.0.1:8000/>)

- Na URL depois do `8000` dígite `auth/cadastro/` ou para acessar a área administrativa `admin/`.

- Na área administrativa coloque o usuário e senha criados na [etapa 8](https://github.com/ShadowsS01/FreelaWay#8-criando-o-super-usu%C3%A1rio).

- **Agora você pode olhar tudo e descobrir como funciona a aplicação. _Lembrando_ que a URL sempre vai ser [aqui](http://127.0.0.1:8000/auth/cadastro).
Apartir daí crie um usuário e entre na home do site fazendo o login.**

## Deploy

O deploy da aplicação foi feito no [Heroku](https://devcenter.heroku.com/).

## Licença

Este projeto esta sobe a licença [MIT](LICENSE)
