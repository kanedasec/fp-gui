# 🧾 Gerador de Justificativas de Falsos Positivos (FP-GUI)

Aplicativo desktop em Python com **interface gráfica (Tkinter + ttkbootstrap)** para gerar relatórios de **justificativas de falsos positivos** em formato **DOCX**.

---

## 🚀 Funcionalidades

✅ Interface com [ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap)  
✅ Suporte a múltiplas **origens de vulnerabilidade**:
✅ Formulários dinâmicos — os campos se ajustam conforme a origem  
✅ Anexo de evidências (imagens)  
✅ Geração automática de relatório `.docx` formatado  
✅ Empacotamento em executável via **PyInstaller**

---

## 🏗️ Estrutura do Projeto

fp-gui/

├── main.py # GUI principal

├── functions.py # Funções auxiliares

├── doc.py # Geração do relatório DOCX

├── data.py # Estrutura de dados e origens

├── logo.png # Logo da empresa/time de segurança

├── build.py # Script para empacotar o app

└── requirements.txt


---

## 💻 Como rodar localmente

### 1️⃣   Clonar o repositório 
```
git clone https://github.com/seuusuario/fp-gui.git
cd fp-gui
```

### 2️⃣   Criar o ambiente virtual
```
python -m venv .venv
source .venv/bin/activate    # Linux
# ou
.venv\Scripts\activate       # Windows
```

### 3️⃣ Instalar as dependências
```
pip install -r requirements.txt
```

### 4️⃣ Executar o aplicativo
```
python main.py
```

### ⚙️ Gerar o Executável

Com o ambiente ativado:
```
python build.py
```

O executável será gerado em:

dist/fp-gui.exe

📄 Relatório Gerado

O relatório .docx contém:

    Informações do projeto (com base na origem)

    Vulnerabilidades justificadas

    Justificativas detalhadas

    Evidências anexadas (quando houver)

    Espaço para aprovação pelo time de segurança

### 🛡️ Desenvolvido por

Kanedasec

### 📦 Licença

Este projeto é de código aberto sob a licença MIT.
Você pode usar, modificar e distribuir livremente, desde que mantenha os créditos ao autor original.

O software é fornecido “no estado em que se encontra”, sem garantias de qualquer tipo.
O uso é permitido apenas para fins legítimos, educacionais ou corporativos, nunca para atividades maliciosas.

---
