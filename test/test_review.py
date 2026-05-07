# python -m pytest

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# Função auxiliar para criar uma review antes de testar a exclusão
def create_review():
    response = client.post(
        "/reviews/", json={"media_id": 5, "rating": 4.5, "comment": "teste"}
    )

    return response.json()


# Testes para as rotas de review
def test_get_reviews():
    response = client.get("/reviews/")

    assert response.status_code == 200


# Testa criação de review com dados válidos
def test_create_review():
    response = client.post(
        "/reviews/", json={"media_id": 5, "rating": 4.5, "comment": "teste"}
    )

    assert response.status_code == 200


# Testa exclusão de review
def test_delete_review():
    review = create_review()  # cria uma review antes de deletar
    response = client.delete(f"/reviews/{review['id_']}")
    assert response.status_code == 204
