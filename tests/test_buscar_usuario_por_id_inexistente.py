import requests
from conftest import BASE_URL


def test_buscar_usuario_por_id_inexistente():
    resposta = requests.get(f"{BASE_URL}/usuarios/idquenaoeexiste12")
    corpo = resposta.json()
    assert resposta.status_code == 400
    assert "message" in corpo or "id" in corpo
