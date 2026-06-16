from conftest import BASE_URL
from conftest import BASE_URL, cadastrar_usuario
from conftest import BASE_URL, cadastrar_usuario, email_unico
from conftest import BASE_URL, email_unico
from jsonschema import validate
from schemas import SCHEMA_LISTAR_USUARIOS
import requests

def test_atualizar_usuario_com_sucesso(usuario_criado):
    payload = {
        "nome": "Nome Atualizado",
        "email": email_unico(),
        "password": "novasenha456",
        "administrador": "true",
    }
    resposta = requests.put(f"{BASE_URL}/usuarios/{usuario_criado}", json=payload)
    assert resposta.status_code == 200
    assert resposta.json()["message"] == "Registro alterado com sucesso"

def test_atualizar_usuario_inexistente_cria_novo():
    payload = {
        "nome": "Usuário Novo Via PUT",
        "email": email_unico(),
        "password": "senha789",
        "administrador": "false",
    }
    resposta = requests.put(f"{BASE_URL}/usuarios/idquenaoexiste999", json=payload)
    assert resposta.status_code == 201
    assert resposta.json()["message"] == "Cadastro realizado com sucesso"

def test_buscar_usuario_por_id_existente(usuario_criado):
    resposta = requests.get(f"{BASE_URL}/usuarios/{usuario_criado}")
    corpo = resposta.json()
    assert resposta.status_code == 200
    assert corpo["_id"] == usuario_criado
    assert "nome" in corpo
    assert "email" in corpo

def test_buscar_usuario_por_id_inexistente():
    resposta = requests.get(f"{BASE_URL}/usuarios/idquenaoeexiste12")
    corpo = resposta.json()
    assert resposta.status_code == 400
    assert "message" in corpo or "id" in corpo

def test_cadastrar_usuario_com_email_duplicado():
    email = email_unico()
    cadastrar_usuario(email=email)
    resposta = cadastrar_usuario(email=email)
    assert resposta.status_code == 400
    assert "já está sendo usado" in resposta.json()["message"]

def test_cadastrar_usuario_sem_campo_administrador():
    payload = {"nome": "Sem Admin", "email": email_unico(), "password": "senha123"}
    resposta = requests.post(f"{BASE_URL}/usuarios", json=payload)
    assert resposta.status_code == 400
    assert "administrador" in resposta.json()

def test_cadastrar_usuario_sem_campo_email():
    payload = {"nome": "Sem Email", "password": "senha123", "administrador": "false"}
    resposta = requests.post(f"{BASE_URL}/usuarios", json=payload)
    assert resposta.status_code == 400
    assert "email" in resposta.json()

def test_cadastrar_usuario_sem_campo_nome():
    payload = {"email": email_unico(), "password": "senha123", "administrador": "false"}
    resposta = requests.post(f"{BASE_URL}/usuarios", json=payload)
    assert resposta.status_code == 400
    assert "nome" in resposta.json()

def test_cadastrar_usuario_sem_campo_password():
    payload = {"nome": "Sem Senha", "email": email_unico(), "administrador": "false"}
    resposta = requests.post(f"{BASE_URL}/usuarios", json=payload)
    assert resposta.status_code == 400
    assert "password" in resposta.json()

def test_cadastrar_usuario_valido():
    resposta = cadastrar_usuario()
    corpo = resposta.json()
    assert resposta.status_code == 201
    assert corpo["message"] == "Cadastro realizado com sucesso"
    assert "_id" in corpo

def test_excluir_usuario_com_sucesso():
    resposta_cadastro = cadastrar_usuario()
    id_usuario = resposta_cadastro.json()["_id"]
    resposta_delete = requests.delete(f"{BASE_URL}/usuarios/{id_usuario}")
    assert resposta_delete.status_code == 200
    assert resposta_delete.json()["message"] == "Registro excluído com sucesso"

def test_excluir_usuario_inexistente():
    resposta = requests.delete(f"{BASE_URL}/usuarios/idquenaoexiste000")
    assert resposta.status_code == 200
    assert resposta.json()["message"] == "Nenhum registro excluído"

def test_listar_usuarios_retorna_campos_esperados():
    resposta = requests.get(f"{BASE_URL}/usuarios")
    corpo = resposta.json()
    
    validate(instance=corpo, schema=SCHEMA_LISTAR_USUARIOS)

def test_listar_usuarios_retorna_status_200():
    resposta = requests.get(f"{BASE_URL}/usuarios")
    assert resposta.status_code == 200

