from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


# Testa a rota raiz para verificar se a API está funcionando
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "API Pycine funcionando"}


def test_get_media():
    pass


def test_create_media():
    pass


def test_update_media():
    pass


def test_delete_media():
    pass