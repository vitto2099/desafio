import subprocess
import sys
from pathlib import Path

PASTA_TESTS = Path(__file__).parent
PASTA_RAIZ = PASTA_TESTS.parent

subprocess.run(
    [sys.executable, "-m", "pip", "install", "--upgrade", "-r", str(PASTA_RAIZ / "requirements.txt")],
    check=True,
)

testes = [
    "test_listar_usuarios_retorna_status_200.py",
    "test_listar_usuarios_retorna_campos_esperados.py",
    "test_cadastrar_usuario_valido.py",
    "test_cadastrar_usuario_com_email_duplicado.py",
    "test_cadastrar_usuario_sem_campo_nome.py",
    "test_cadastrar_usuario_sem_campo_email.py",
    "test_cadastrar_usuario_sem_campo_password.py",
    "test_buscar_usuario_por_id_existente.py",
    "test_buscar_usuario_por_id_inexistente.py",
    "test_atualizar_usuario_com_sucesso.py",
    "test_atualizar_usuario_inexistente_cria_novo.py",
    "test_excluir_usuario_com_sucesso.py",
    "test_excluir_usuario_inexistente.py",
    "test_cadastrar_usuario_sem_campo_administrador.py",
]

if __name__ == "__main__":
    arquivos = [str(PASTA_TESTS / t) for t in testes]
    resultado = subprocess.run(
        [sys.executable, "-m", "pytest", "-v"] + arquivos,
        cwd=str(PASTA_RAIZ),
    )
    sys.exit(resultado.returncode)
