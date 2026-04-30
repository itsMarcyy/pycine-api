# Pycine 🎬

API desenvolvida com FastAPI para gerenciamento de mídias e avaliações.

## 🚧 Status
Projeto em desenvolvimento.

## 🛠 Tecnologias
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic

## ⚙️ Funcionalidades
- Cadastro e listagem de mídias  
- Sistema de avaliações  
- Validação de nota (1 a 5 com intervalo de 0.5)  

## 📌 Próximos passos
- Autenticação de usuários
- Sistema de favoritos
- Melhorias na estrutura do projeto

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
