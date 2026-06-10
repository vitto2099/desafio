import requests
from conftest import BASE_URL


def test_listar_usuarios_retorna_status_200():
    resposta = requests.get(f"{BASE_URL}/usuarios")
    assert resposta.status_code == 200
