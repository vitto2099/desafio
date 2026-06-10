import requests
from conftest import BASE_URL


def test_excluir_usuario_inexistente():
    resposta = requests.delete(f"{BASE_URL}/usuarios/idquenaoexiste000")
    assert resposta.status_code == 200
    assert resposta.json()["message"] == "Nenhum registro excluído"
