# main.py
import os
import sys
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from utils.data import ORIGENS
from functions.functions import handle_anexar_evidencia, handle_adicionar_justificativa, delete_selected_item, clean_items
from functions.doc import criar_report


# ===============================================================
# Helper PyInstaller
# ===============================================================
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("")
    return os.path.join(base_path, relative_path)


# ===============================================================
# Funções de Renderização
# ===============================================================
def render_generic_form(frame, campos):
    """Cria dinamicamente campos (entry, combobox, checkbox, etc.)"""
    for w in frame.winfo_children():
        w.destroy()

    widgets = {}
    for campo in campos:
        tb.Label(frame, text=campo["label"]).pack(anchor=W, pady=2)
        tipo = campo["type"]

        if tipo == "entry":
            entry = tb.Entry(frame)
            entry.pack(fill=X, pady=2)
            widgets[campo["label"]] = entry
        elif tipo == "combobox":
            combo = tb.Combobox(frame, values=campo.get("values", []), state="readonly")
            combo.pack(fill=X, pady=2)
            widgets[campo["label"]] = combo
        elif tipo == "checkbox":
            var = tk.IntVar()
            chk = tb.Checkbutton(frame, text=campo["label"], variable=var)
            chk.pack(anchor=W)
            widgets[campo["label"]] = var
        elif tipo == "radiobutton":
            var = tk.StringVar()
            for val in campo["values"]:
                rb = tb.Radiobutton(frame, text=val, value=val, variable=var)
                rb.pack(anchor=W)
            widgets[campo["label"]] = var
        elif tipo == "text":
            text = tk.Text(frame, height=5)
            text.pack(fill=BOTH, pady=2)
            widgets[campo["label"]] = text
    return widgets


# ===============================================================
# Função principal
# ===============================================================
def main():
    app = tb.Window(themename="pulse")
    app.title("Gerador de Justificativas")
    app.geometry("1100x800")

   # Bloco para permitir escolha do tema em tempo real
    style = app.style
    temas = {"Dia": "pulse", "Noite": "superhero"}

    tema_frame = tb.Frame(app, padding=(5, 0))
    tema_frame.pack(fill=X, padx=10, pady=(5, 0))

    tb.Label(tema_frame, text="Tema: ").pack(side=LEFT, padx=(0, 5))

    tema_combobox = tb.Combobox(
        tema_frame,
        values=list(temas.keys()),
        state="readonly",
        width=15
    )
    tema_combobox.set("Dia")
    tema_combobox.pack(side=LEFT)

    def trocar_tema(event=None):
        tema_selecionado = tema_combobox.get()
        novo_tema = temas.get(tema_selecionado, style.theme_use())
        try:
            style.theme_use(novo_tema)
        except Exception as e:
            messagebox.showerror("Erro ao aplicar tema", str(e))
        

    tema_combobox.bind("<<ComboboxSelected>>", trocar_tema)
    # Fim do bloco para escolha do tema em real time

    main_pane = tb.Panedwindow(app, orient=HORIZONTAL)
    main_pane.pack(fill=BOTH, expand=True, padx=10, pady=10)

    left_frame = tb.Frame(main_pane, padding=10)
    main_pane.add(left_frame, weight=1)

    right_frame = tb.Frame(main_pane, padding=10)
    main_pane.add(right_frame, weight=2)

    # ===========================================================
    # BLOCO 1: ORIGEM DA VULNERABILIDADE
    # ===========================================================
    origem_labelframe = tb.Labelframe(left_frame, text="Origem da Vulnerabilidade", padding=10)
    origem_labelframe.pack(fill=X, pady=5)

    tb.Label(origem_labelframe, text="Selecione a origem:").pack(anchor=W)
    origem_combobox = tb.Combobox(origem_labelframe, values=list(ORIGENS.keys()), state="readonly")
    origem_combobox.pack(fill=X, pady=5)

    # ===========================================================
    # BLOCO 2: DADOS DA APLICAÇÃO
    # ===========================================================
    dados_frame = tb.Labelframe(left_frame, text="Dados da Aplicação", padding=10)
    dados_frame.pack(fill=X, pady=5)

    dados_widgets = {}

    # ===========================================================
    # BLOCO 3: TIPO DE VULNERABILIDADE
    # ===========================================================
    vuln_frame = tb.Labelframe(left_frame, text="Tipo de Vulnerabilidade", padding=10)
    vuln_frame.pack(fill=BOTH, expand=True, pady=5)

    tipo_vuln = tb.Entry(vuln_frame)
    tipo_vuln.pack(fill=X, pady=(0, 5))

    lista_vuln = tk.Listbox(vuln_frame, height=8)
    lista_vuln.pack(fill=BOTH, expand=True)

    def select_vuln(event):
        sel = lista_vuln.curselection()
        if sel:
            tipo_vuln.delete(0, tk.END)
            tipo_vuln.insert(0, lista_vuln.get(sel[0]))

    lista_vuln.bind("<ButtonRelease-1>", select_vuln)

    # ===========================================================
    # BLOCO 4: FORMULÁRIO DE JUSTIFICATIVA
    # ===========================================================
    form_frame = tb.Labelframe(right_frame, text="Formulário de Justificativa", padding=10)
    form_frame.pack(fill=BOTH, expand=True, pady=5)

    justific_widgets = {}

    # ===========================================================
    # BLOCO 5: LISTA DE JUSTIFICATIVAS
    # ===========================================================
    lista_labelframe = tb.Labelframe(right_frame, text="Lista de Justificativas", padding=10)
    lista_labelframe.pack(fill=BOTH, expand=True, pady=5)

    lista_justificativa = tk.Listbox(lista_labelframe, height=10)
    lista_justificativa.pack(fill=BOTH, expand=True)
    lista_justificativa.bind("<Delete>", lambda e: delete_selected_item(lista_justificativa))
    
    

    # ===========================================================
    # BOTÕES
    # ===========================================================
    btn_frame = tb.Frame(right_frame)
    btn_frame.pack(fill=X, pady=10)

    tb.Button(btn_frame, text="Anexar Evidência", bootstyle=SECONDARY,
              command=handle_anexar_evidencia).pack(side=LEFT, padx=5)

    tb.Button(
        btn_frame,
        text="Adicionar Justificativa",
        bootstyle=INFO,
        command=lambda: handle_adicionar_justificativa(
            justific_widgets,
            lista_justificativa,
            origem_combobox.get(),
            tipo_vuln.get()
        )
    ).pack(side=LEFT, padx=5)
    
    tb.Button(
        btn_frame,
        text="Deletar Justificativa",
        bootstyle=WARNING,
        command=lambda: delete_selected_item(lista_justificativa)
    ).pack(side=LEFT, padx=5)

    def gerar_relatorio_func():
        tuple_justificativa = lista_justificativa.get(0, tk.END)
        respostas_app = {lbl: w.get() if hasattr(w, "get") else "" for lbl, w in dados_widgets.items()}    
        
        if origem_combobox.get() == "BSV": 
       
            if any(valor.strip() == "" for chave, valor in respostas_app.items() if chave != "Nome do Serviço/Hostname"):
                messagebox.showwarning("Validação", "Preencha todos os dados da aplicação.")
                return
        else:
             if any(valor.strip() == "" for valor in respostas_app.values()):
                messagebox.showwarning("Validação", "Preencha todos os dados da aplicação.")
                return 
     
        if not tuple_justificativa:
            messagebox.showwarning("Validação", "Adicione pelo menos uma justificativa.")
            return

        logo = resource_path("utils/logo.png") if os.path.exists("utils/logo.png") else None
        try:
            criar_report(logo, list(respostas_app.values()), tuple_justificativa)
            messagebox.showinfo("Relatório", "Relatório DOCX gerado com sucesso! ✅")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    tb.Button(btn_frame, text="Gerar Relatório", bootstyle=SUCCESS,
              command=gerar_relatorio_func).pack(side=RIGHT, padx=5)
    
    tb.Button(
        btn_frame,
        text="Limpar Justificativas",
        bootstyle=DANGER,
        command=lambda: clean_items(lista_justificativa)
    ).pack(side=RIGHT, padx=5)

    # ===========================================================
    # EVENTO: MUDANÇA DE ORIGEM
    # ===========================================================
    def on_origem_change(event):
        nonlocal dados_widgets, justific_widgets
        origem = origem_combobox.get()
        config = ORIGENS.get(origem, {})

        # Renderiza novos blocos
        dados_widgets = render_generic_form(dados_frame, config.get("dados_aplicacao", []))
        justific_widgets = render_generic_form(form_frame, config.get("formulario", []))
        
        # Atualiza lista de vulnerabilidades
        lista_vuln.delete(0, tk.END)
        for v in config.get("vulnerabilidades", []):
            lista_vuln.insert(tk.END, v)

    origem_combobox.bind("<<ComboboxSelected>>", on_origem_change)

    app.mainloop()


if __name__ == "__main__":
    main()
