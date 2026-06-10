import requests
from conftest import BASE_URL, cadastrar_usuario, email_unico


def test_cadastrar_usuario_com_email_duplicado():
    email = email_unico()
    cadastrar_usuario(email=email)
    resposta = cadastrar_usuario(email=email)
    assert resposta.status_code == 400
    assert "já está sendo usado" in resposta.json()["message"]
