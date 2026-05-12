from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# Testa a rota raiz para verificar se a API está funcionando
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "API Pycine funcionando"}


# Testes para as rotas de mídia
def test_get_media():
    response = client.get("/media")

    assert response.status_code == 200


# Testa criação de mídia com dados válidos
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


# Testa atualização de mídia
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


# Testa exclusão de mídia
def test_delete_media():
    response = client.delete("/media/1")
    assert response.status_code == 204
