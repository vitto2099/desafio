import requests
from conftest import BASE_URL


def test_buscar_usuario_por_id_existente(usuario_criado):
    resposta = requests.get(f"{BASE_URL}/usuarios/{usuario_criado}")
    corpo = resposta.json()
    assert resposta.status_code == 200
    assert corpo["_id"] == usuario_criado
    assert "nome" in corpo
    assert "email" in corpo
