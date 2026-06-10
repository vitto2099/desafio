import requests
from conftest import BASE_URL


def test_listar_usuarios_retorna_campos_esperados():
    resposta = requests.get(f"{BASE_URL}/usuarios")
    corpo = resposta.json()
    assert "quantidade" in corpo
    assert "usuarios" in corpo
    assert isinstance(corpo["usuarios"], list)
