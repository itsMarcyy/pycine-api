# Pycine 🎬

API desenvolvida com FastAPI para gerenciamento de mídias e avaliações, com autenticação JWT e controle de acesso por usuário.

## 🚧 Status
Projeto em desenvolvimento.

## 🛠 Tecnologias
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- JWT
- Pytest

## ⚙️ Funcionalidades

## Usuários
- Cadastro de usuários
- Login com autenticação JWT

## Midia
- Cadastro de mídias
- Listagem de mídias
- Atualização e remoção de mídias
- Associação de mídias ao usuário autenticado

## Avaliações
- Cadastro de avaliações
- Listagem de avaliações
- Validação de notas (1 a 5 com intervalos de 0.5)
- Associação de avaliações ao usuário autenticado
- Cálculo da média de avaliações por mídia

##📂 Estrutura do Projeto
- Organização modular utilizando FastAPI
- Schemas com Pydantic
- Banco de dados PostgreSQL
- Autenticação baseada em JWT
- Testes automatizados para módulos de mídias e avaliações

## 📌 Próximos passos
- Sistema de favoritos
- Melhorias na estrutura do projeto
- Melhorias na documentação

## ▶️ Como rodar o projeto

```bash
git clone https://github.com/itsMarcyy/pycine-api
cd pycine-api

# ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows

# dependências
pip install -r requirements.txt

# servidor
uvicorn app.main:app --reload
