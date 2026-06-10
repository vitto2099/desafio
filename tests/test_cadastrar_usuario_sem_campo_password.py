import requests
from conftest import BASE_URL, email_unico


def test_cadastrar_usuario_sem_campo_password():
    payload = {"nome": "Sem Senha", "email": email_unico(), "administrador": "false"}
    resposta = requests.post(f"{BASE_URL}/usuarios", json=payload)
    assert resposta.status_code == 400
    assert "password" in resposta.json()
