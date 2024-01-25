
# Personal Finance Control - Controle de Finanças Pessoais

Aplicativo de Controle de Finanças Pessoais feito com Python e Django para a disciplina de Análise e Projeto de Sistemas, ministrada pelo professor **Marco Antônio**.

**Instituto Federal do Piauí - Campus Picos** 

## Começando

Essas instruções fornecerão uma cópia do projeto em execução na sua máquina local para fins de teste. Esse projeto visa demonstrar a aplicabilidade do desenvolvimento ágil na programação. 

**Versão do Python**: `3.11.2`

**Versão do Django**: `4.1.3`

**Sistema operacional:** `Ubuntu`

O gerenciameto de dependências é feito usando o pip. Caso ocorra erros ao executar o aplicativo, tente seguir as instruções abaixo:

### Iniciando o projeto com o `virtualenv`

***É recomendado que instale o virtualenv na sua máquina para separar o ambiente de desenvolvimento do ambiente global.***

Ignore os passos à seguir se for instalar as dependências no seu ambiente global.

*Execute o seguinte comando para criar uma `virtualenv`:*

```bash
virtualenv [nome da env]
```

***O comando acima irá criar um abiente de desenvolvimento***

*Agora, vamos entrar no ambiente virtual com o seguinte comando:*

```bash
source env/bin/activate
```

## Instalando os requerimentos

*Execute o seguinte comando para instalar os requerimentos do sistema:*

```bash
pip install -r requirements.txt
```

## Instruções para o Banco de Dados
O banco de dados utilizado é o SQLite, padrão do framework Django. Abaixo segue o tutorial de como criar o banco de dados para rodar o sistema:

Primeiramente, crie uma nova `migrations`

*Execute o comando:*

```bash
python manage.py makemigrations
```

*E logo após:*

```bash
python manage.py migrate
```

Seu banco de dados SQLite irá ser criado.

## Criando um usuário administrador

*Para ter acesso ao sistema, será necessário criar um `superusuário`:*

```bash
python manage.py createsuperuser
```

Após criar o usuário com as suas credenciais você estará habilitado a entrar no sistema.

## Iniciando o servidor local

*Para iniciar o servidor `local`, basta executar o seguinte comando no seu terminal:*

```bash
python manage.py runserver
```

Agora, basta entrar no link fornecido no seu terminal em qualquer navegador instalado na sua máquina

## Desenvolvedores

- [![Avelar Rodrigues](https://img.shields.io/badge/avelando-GitHub-blueviolet)](https://github.com/avelando)
- [![Jean Carlos](https://img.shields.io/badge/JeanCarlos899-GitHub-blueviolet)](https://github.com/JeanCarlos899)
- [![Karielly de Carvalho](https://img.shields.io/badge/Kariellyy-GitHub-blueviolet)](https://github.com/Kariellyy)

<hr>
