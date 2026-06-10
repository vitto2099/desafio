import requests
from conftest import BASE_URL, email_unico


def test_cadastrar_usuario_sem_campo_nome():
    payload = {"email": email_unico(), "password": "senha123", "administrador": "false"}
    resposta = requests.post(f"{BASE_URL}/usuarios", json=payload)
    assert resposta.status_code == 400
    assert "nome" in resposta.json()
