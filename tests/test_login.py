from jsonschema import validate
from conftest import email_unico, cadastrar_usuario, fazer_login
from schemas import SCHEMA_LOGIN_SUCESSO


def test_login_com_credenciais_corretas():
    email = email_unico()
    senha = "minhasenha123"
    cadastrar_usuario(email=email, password=senha)
    
    resposta = fazer_login(email, senha)
    corpo = resposta.json()
    
    assert resposta.status_code == 200
    validate(instance=corpo, schema=SCHEMA_LOGIN_SUCESSO)


def test_login_com_senha_errada():
    email = email_unico()
    senha_correta = "senha_correta"
    cadastrar_usuario(email=email, password=senha_correta)
    
    resposta = fazer_login(email, "senha_errada")
    corpo = resposta.json()
    
    assert resposta.status_code == 401
    assert corpo["message"] == "Email e/ou senha inválidos"


def test_login_com_email_inexistente():
    email_nao_cadastrado = email_unico()
    
    resposta = fazer_login(email_nao_cadastrado, "qualquersenha")
    corpo = resposta.json()
    
    assert resposta.status_code == 401
    assert corpo["message"] == "Email e/ou senha inválidos"


def test_login_com_campos_vazios():
    resposta_email_vazio = fazer_login("", "senha123")
    assert resposta_email_vazio.status_code == 400
    assert "email não pode ficar em branco" in resposta_email_vazio.json()["email"]
    
    resposta_senha_vazia = fazer_login(email_unico(), "")
    assert resposta_senha_vazia.status_code == 400
    assert "password não pode ficar em branco" in resposta_senha_vazia.json()["password"]
