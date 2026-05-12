# python -m pytest

from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def create_review():
    response = client.post(
        "/reviews", json={
            "media_id": 1, 
            "rating": 4.5, 
            "comment": "teste"}
    )

    return response.json()


def test_get_reviews():
    response = client.get("/reviews")

    assert response.status_code == 200


# Criação de review com dados válidos
def test_create_review():
    response = client.post(
        "/reviews", json={
            "media_id": 1, 
            "rating": 4.5, 
            "comment": "teste"}
    )

    assert response.status_code == 200


def test_update_review():
    review = create_review()  # cria uma review antes de atualizar
    response = client.put(
        f"/reviews/{review['id_']}",
        json={
            "media_id": 1, 
            "rating": 4.0, 
            "comment": "teste atualizado"},
    )

    assert response.status_code == 200


def test_delete_review():
    review = create_review()  # cria uma review antes de deletar
    response = client.delete(f"/reviews/{review['id_']}")
    assert response.status_code == 204
