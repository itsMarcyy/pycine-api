from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_media():
    response = client.get("/media")

    assert response.status_code == 200


# Criação de mídia com dados válidos
def test_create_media():
    response = client.post(
        "/media",
        json={
            "title": "Teste",
            "media_type": "movie",
            "release_year": 2024,
            "genre": "Terror",
        },
    )

    assert response.status_code == 200


# Criação de mídia com tipo inválido
def test_create_media_invalid_type():
    response = client.post(
        "/media",
        json={
            "title": "Teste",
            "media_type": "filme",  
            "release_year": 2024,
            "genre": "Terror",
        },
    )

    assert response.status_code == 422


def test_update_media():
    response = client.put(
        "/media/1",
        json={
            "title": "Teste Atualizado",
            "media_type": "movie",
            "release_year": 2024,
            "genre": "Terror",
        },
    )

    assert response.status_code == 200


def test_delete_media():
    response = client.delete("/media/1")
    assert response.status_code == 204
