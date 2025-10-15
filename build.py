import os
import PyInstaller.__main__

# Caminho base do projeto
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Nome do executável
APP_NAME = "fp-gui"

# Caminho do logo
LOGO_PATH = os.path.join(BASE_DIR, "logo.png")

PyInstaller.__main__.run([
    "main.py",
    "--name", APP_NAME,
    "--onefile",               # gera apenas um executável
    "--noconsole",             # não abre console (para GUI)
    f"--add-data={LOGO_PATH}{os.pathsep}.",  # inclui o logo.png no pacote
    "--hidden-import=ttkbootstrap",
    "--hidden-import=docx",
    "--hidden-import=data",
    "--hidden-import=functions",
    "--hidden-import=doc",
])
