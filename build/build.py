import os
import sys
import shutil
import PyInstaller.__main__

# =============================================================
# CONFIGURAÇÕES BÁSICAS
# =============================================================

# Caminho base do projeto (raiz)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# Caminho do arquivo principal
MAIN_FILE = os.path.join(BASE_DIR, "main.py")

# Caminho do logo (dentro de utils/)
LOGO_PATH = os.path.join(BASE_DIR, "utils", "logo.png")

# Nome do executável
APP_NAME = "fp-gui"

# Caminhos de saída
DIST_DIR = os.path.join(BASE_DIR, "dist")
BUILD_DIR = os.path.join(BASE_DIR, "build", "temp_build")

# =============================================================
# LIMPEZA DE BUILDS ANTIGOS
# =============================================================
print("🧹 Limpando builds anteriores...")
for path in [DIST_DIR, BUILD_DIR]:
    if os.path.exists(path):
        shutil.rmtree(path)
        print(f" - Removido: {path}")

# =============================================================
# VERIFICAÇÕES
# =============================================================
if not os.path.exists(MAIN_FILE):
    print(f"❌ ERRO: Arquivo principal não encontrado em: {MAIN_FILE}")
    sys.exit(1)

if not os.path.exists(LOGO_PATH):
    print(f"⚠️  Aviso: Logo não encontrado em: {LOGO_PATH} (será ignorado)")
    ADD_DATA = ""
else:
    # O PyInstaller usa separador `;` no Windows e `:` no Linux/macOS
    ADD_DATA = f"--add-data={LOGO_PATH}{os.pathsep}utils"

# =============================================================
# EXECUÇÃO DO BUILD
# =============================================================
print("🚀 Iniciando build com PyInstaller...\n")

PyInstaller.__main__.run([
    MAIN_FILE,
    "--name", APP_NAME,
    "--onefile",               # gera executável único
    "--noconsole",             # oculta o console (para GUI)
    ADD_DATA,
    "--hidden-import=ttkbootstrap",
    "--hidden-import=docx",
    "--hidden-import=data",
    "--hidden-import=functions",
    "--hidden-import=doc",
    "--workpath", BUILD_DIR,
    "--distpath", DIST_DIR,
])

# =============================================================
# RESULTADO
# =============================================================
print("\n✅ Build concluído com sucesso!")
print(f"📦 Executável gerado em: {os.path.join(DIST_DIR, APP_NAME)}")
print("🎨 Logo incluído em utils/ dentro do pacote.")
