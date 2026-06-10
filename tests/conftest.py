import uuid
import pytest
import requests

BASE_URL = "https://compassuol.serverest.dev"


def email_unico():
    return f"teste_{uuid.uuid4().hex[:8]}@qa.com"


def cadastrar_usuario(nome=None, email=None, password=None, administrador=None):
    payload = {
        "nome": nome or "Usuário Teste",
        "email": email or email_unico(),
        "password": password or "senha123",
        "administrador": administrador if administrador is not None else "false",
    }
    return requests.post(f"{BASE_URL}/usuarios", json=payload)


@pytest.fixture
def usuario_criado():
    resposta = cadastrar_usuario()
    dados = resposta.json()
    yield dados["_id"]
    requests.delete(f"{BASE_URL}/usuarios/{dados['_id']}")
