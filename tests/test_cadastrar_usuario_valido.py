import requests
from conftest import BASE_URL, cadastrar_usuario


def test_cadastrar_usuario_valido():
    resposta = cadastrar_usuario()
    corpo = resposta.json()
    assert resposta.status_code == 201
    assert corpo["message"] == "Cadastro realizado com sucesso"
    assert "_id" in corpo
