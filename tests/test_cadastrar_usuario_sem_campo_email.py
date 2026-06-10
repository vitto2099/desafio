import requests
from conftest import BASE_URL


def test_cadastrar_usuario_sem_campo_email():
    payload = {"nome": "Sem Email", "password": "senha123", "administrador": "false"}
    resposta = requests.post(f"{BASE_URL}/usuarios", json=payload)
    assert resposta.status_code == 400
    assert "email" in resposta.json()
