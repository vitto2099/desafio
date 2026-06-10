import requests
from conftest import BASE_URL, email_unico


def test_atualizar_usuario_com_sucesso(usuario_criado):
    payload = {
        "nome": "Nome Atualizado",
        "email": email_unico(),
        "password": "novasenha456",
        "administrador": "true",
    }
    resposta = requests.put(f"{BASE_URL}/usuarios/{usuario_criado}", json=payload)
    assert resposta.status_code == 200
    assert resposta.json()["message"] == "Registro alterado com sucesso"
