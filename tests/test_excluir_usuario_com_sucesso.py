import requests
from conftest import BASE_URL, cadastrar_usuario


def test_excluir_usuario_com_sucesso():
    resposta_cadastro = cadastrar_usuario()
    id_usuario = resposta_cadastro.json()["_id"]
    resposta_delete = requests.delete(f"{BASE_URL}/usuarios/{id_usuario}")
    assert resposta_delete.status_code == 200
    assert resposta_delete.json()["message"] == "Registro excluído com sucesso"
