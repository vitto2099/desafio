# Testes Automatizados — ServeRest `/usuarios`

Projeto de testes automatizados em **Python + Pytest** para o endpoint de Usuários da API pública [ServeRest](https://compassuol.serverest.dev/).

---

## O que é cada coisa?

### 🐍 Python
Linguagem de programação usada para escrever os testes. Todo arquivo `.py` é um arquivo Python.

### ✅ Pytest
Framework de testes para Python. Ele encontra automaticamente qualquer função que comece com `test_` e executa como um teste. Ao final, mostra quais passaram (`PASSED`) e quais falharam (`FAILED`).

### 🌐 Requests
Biblioteca Python para fazer chamadas HTTP (GET, POST, PUT, DELETE) — é com ela que os testes "conversam" com a API.

### 🔗 ServeRest
API REST pública que simula uma loja virtual. Os testes utilizam o endpoint `/usuarios`, que permite listar, cadastrar, buscar, atualizar e excluir usuários.

---

## Estrutura do projeto

```
Pytest/
│
├── tests/                                              ← pasta com todos os testes
│   │
│   ├── conftest.py                                     ← configurações e funções compartilhadas
│   ├── test_rodarTudo.py                               ← script que executa os 14 testes de uma vez
│   │
│   ├── test_listar_usuarios_retorna_status_200.py
│   ├── test_listar_usuarios_retorna_campos_esperados.py
│   ├── test_cadastrar_usuario_valido.py
│   ├── test_cadastrar_usuario_com_email_duplicado.py
│   ├── test_cadastrar_usuario_sem_campo_nome.py
│   ├── test_cadastrar_usuario_sem_campo_email.py
│   ├── test_cadastrar_usuario_sem_campo_password.py
│   ├── test_buscar_usuario_por_id_existente.py
│   ├── test_buscar_usuario_por_id_inexistente.py
│   ├── test_atualizar_usuario_com_sucesso.py
│   ├── test_atualizar_usuario_inexistente_cria_novo.py
│   ├── test_excluir_usuario_com_sucesso.py
│   ├── test_excluir_usuario_inexistente.py
│   └── test_cadastrar_usuario_sem_campo_administrador.py
│
├── pytest.ini                                          ← configurações do Pytest
├── requirements.txt                                    ← lista de dependências
└── README.md                                           ← este arquivo
```

---

## O que é o `conftest.py`?

O `conftest.py` é um arquivo especial reconhecido automaticamente pelo Pytest. Ele centraliza tudo que é compartilhado entre os testes:

- **`BASE_URL`** — endereço da API (`https://compassuol.serverest.dev`)
- **`email_unico()`** — gera um email aleatório a cada chamada para evitar conflito entre testes
- **`cadastrar_usuario()`** — função auxiliar que faz um POST para criar um usuário
- **`usuario_criado`** — *fixture*: cria um usuário antes do teste e o apaga depois automaticamente

### O que é uma fixture?
Uma fixture (`@pytest.fixture`) é uma função que **prepara e limpa dados** para um teste. O trecho `yield` separa o preparo (antes do teste) da limpeza (depois do teste):

```python
@pytest.fixture
def usuario_criado():
    resposta = cadastrar_usuario()   # ← cria o usuário ANTES do teste
    dados = resposta.json()
    yield dados["_id"]               # ← entrega o ID para o teste usar
    requests.delete(...)             # ← apaga o usuário DEPOIS do teste
```

---

## O que é o `pytest.ini`?

Arquivo de configuração do Pytest. Define onde ficam os testes e opções padrão:

```ini
[pytest]
testpaths = tests      ← Pytest vai procurar testes dentro da pasta /tests
addopts = -v --tb=short  ← -v mostra o nome de cada teste; --tb=short mostra erros resumidos
```

---

## O que é o `requirements.txt`?

Lista as bibliotecas externas que o projeto precisa. Basta instalar uma vez:

```
pytest==8.3.5       ← framework de testes
requests==2.32.3    ← para fazer chamadas HTTP
pytest-html==4.1.1  ← para gerar relatório HTML (opcional)
```

---

## Como instalar e rodar

### 1. Pré-requisitos
- [Python 3.9+](https://www.python.org/downloads/) instalado
- Terminal aberto na **pasta raiz do projeto** (`Pytest/`)

### 2. Instale as dependências
> ⚠️ Execute este comando na pasta `Pytest/`, **não** dentro de `tests/`

```bash
pip install -r requirements.txt
```

### 3. Formas de rodar os testes

#### ▶ Rodar tudo de uma vez (recomendado)
```bash
python tests/test_rodarTudo.py
```

#### ▶ Rodar via Pytest diretamente
```bash
python -m pytest -v
```

#### ▶ Rodar um único arquivo de teste
```bash
python -m pytest tests/test_cadastrar_usuario_valido.py -v
```

#### ▶ Rodar um teste específico pelo nome
```bash
python -m pytest -k "test_cadastrar_usuario_valido" -v
```

#### ▶ Gerar relatório HTML
```bash
python -m pytest --html=relatorio.html --self-contained-html
```
Abre o arquivo `relatorio.html` no navegador para ver o resultado visual.

---

## Os 14 testes

| # | Arquivo | O que testa |
|---|---------|-------------|
| 1 | `test_listar_usuarios_retorna_status_200` | A API responde corretamente ao listar usuários |
| 2 | `test_listar_usuarios_retorna_campos_esperados` | A resposta contém `quantidade` e `usuarios` |
| 3 | `test_cadastrar_usuario_valido` | Cadastro com todos os campos → retorna 201 e `_id` |
| 4 | `test_cadastrar_usuario_com_email_duplicado` | Email já usado → retorna 400 |
| 5 | `test_cadastrar_usuario_sem_campo_nome` | Sem `nome` → retorna 400 |
| 6 | `test_cadastrar_usuario_sem_campo_email` | Sem `email` → retorna 400 |
| 7 | `test_cadastrar_usuario_sem_campo_password` | Sem `password` → retorna 400 |
| 8 | `test_buscar_usuario_por_id_existente` | Busca por ID válido → retorna dados do usuário |
| 9 | `test_buscar_usuario_por_id_inexistente` | ID inválido → retorna 400 |
| 10 | `test_atualizar_usuario_com_sucesso` | PUT em usuário existente → retorna 200 |
| 11 | `test_atualizar_usuario_inexistente_cria_novo` | PUT em ID inexistente → API cria novo (201) |
| 12 | `test_excluir_usuario_com_sucesso` | DELETE de usuário existente → retorna 200 |
| 13 | `test_excluir_usuario_inexistente` | DELETE de ID inexistente → "Nenhum registro excluído" |
| 14 | `test_cadastrar_usuario_sem_campo_administrador` | Sem `administrador` → retorna 400 |

---

## Como funciona um teste na prática?

Exemplo do arquivo `test_cadastrar_usuario_valido.py`:

```python
def test_cadastrar_usuario_valido():
    resposta = cadastrar_usuario()          # faz um POST na API com dados válidos
    corpo = resposta.json()                 # converte a resposta para dicionário Python

    assert resposta.status_code == 201      # verifica que o status HTTP é 201 (Criado)
    assert corpo["message"] == "Cadastro realizado com sucesso"  # verifica a mensagem
    assert "_id" in corpo                   # verifica que a API retornou um ID
```

- `assert` → afirma que algo é verdade. Se não for, o teste falha.
- `status_code` → código HTTP da resposta (200 = OK, 201 = Criado, 400 = Erro, etc.)

---

## Por que os emails são dinâmicos?

A ServeRest é uma API pública compartilhada. Se dois testes usassem o mesmo email, o segundo falharia com "email já cadastrado". Para evitar isso, a função `email_unico()` gera um email diferente a cada chamada:

```python
def email_unico():
    return f"teste_{uuid.uuid4().hex[:8]}@qa.com"
    # Exemplo de resultado: teste_a3f7b2c1@qa.com
```

`uuid4()` gera um identificador universalmente único — a chance de colisão é praticamente zero.

---

## Interpretando o resultado

```
PASSED   → o teste passou, o comportamento está correto
FAILED   → o teste falhou, algo não está como esperado
ERROR    → houve um erro antes do teste rodar (ex: problema de conexão)
```

Ao final, o Pytest mostra um resumo:
```
14 passed in 13.87s   ← todos os 14 passaram em ~14 segundos
```
