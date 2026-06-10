import requests
from conftest import BASE_URL, email_unico


def test_atualizar_usuario_inexistente_cria_novo():
    payload = {
        "nome": "Usuário Novo Via PUT",
        "email": email_unico(),
        "password": "senha789",
        "administrador": "false",
    }
    resposta = requests.put(f"{BASE_URL}/usuarios/idquenaoexiste999", json=payload)
    assert resposta.status_code == 201
    assert resposta.json()["message"] == "Cadastro realizado com sucesso"
