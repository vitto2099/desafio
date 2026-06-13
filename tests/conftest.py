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


def fazer_login(email, password):
    payload = {
        "email": email,
        "password": password
    }
    return requests.post(f"{BASE_URL}/login", json=payload)


@pytest.fixture
def token_admin():
    email = email_unico()
    senha = "senhaadmin123"
    resposta_cadastro = cadastrar_usuario(email=email, password=senha, administrador="true")
    id_usuario = resposta_cadastro.json()["_id"]
    
    resposta_login = fazer_login(email, senha)
    token = resposta_login.json().get("authorization")
    
    yield token
    
    requests.delete(f"{BASE_URL}/usuarios/{id_usuario}")


def cadastrar_produto(token, nome=None, preco=None, descricao=None, quantidade=None):
    payload = {
        "nome": nome or f"Produto {uuid.uuid4().hex[:8]}",
        "preco": preco or 150,
        "descricao": descricao or "Descrição do produto teste",
        "quantidade": quantidade or 10
    }
    headers = {"Authorization": token}
    return requests.post(f"{BASE_URL}/produtos", json=payload, headers=headers)

