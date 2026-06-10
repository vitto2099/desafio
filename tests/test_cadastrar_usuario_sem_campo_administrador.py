import requests
from conftest import BASE_URL, email_unico


def test_cadastrar_usuario_sem_campo_administrador():
    payload = {"nome": "Sem Admin", "email": email_unico(), "password": "senha123"}
    resposta = requests.post(f"{BASE_URL}/usuarios", json=payload)
    assert resposta.status_code == 400
    assert "administrador" in resposta.json()
