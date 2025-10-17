# functions.py
import tkinter as tk
from tkinter import filedialog, messagebox
import ttkbootstrap as tb

attached_evidence = []


def handle_anexar_evidencia():
    """Seleciona imagens e adiciona à lista de evidências."""
    global attached_evidence
    files = filedialog.askopenfilenames(
        title="Selecione as evidências",
        filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.gif;*.bmp"), ("Todos", "*.*")]
    )
    if files:
        attached_evidence.extend(files)
        messagebox.showinfo("Sucesso", f"{len(files)} evidência(s) anexada(s). ✅")
    else:
        messagebox.showwarning("Atenção", "Nenhum arquivo selecionado.")


def delete_selected_item(listbox):
    """Remove itens da listbox."""
    selected = listbox.curselection()
    for i in reversed(selected):
        listbox.delete(i)

def clean_items(listbox):
    """Remove todos os itens da listbox."""
    listbox.delete(0, tk.END)


def coletar_valores(widgets_dict):
    """Coleta todos os valores de um conjunto de widgets."""
    dados = {}
    for label, widget in widgets_dict.items():
        if isinstance(widget, tk.Entry):
            dados[label] = widget.get()
        elif isinstance(widget, tk.Text):
            dados[label] = widget.get("1.0", tk.END).strip()
        elif isinstance(widget, tk.IntVar):
            dados[label] = "Sim" if widget.get() == 1 else "Não"
        elif isinstance(widget, tk.StringVar):
            dados[label] = widget.get()
        elif isinstance(widget, tb.Combobox):
            dados[label] = widget.get()
    return dados


def handle_adicionar_justificativa(widgets_dict, lista_justificativa, origem, tipo_vuln):
    """Adiciona a justificativa à lista, incluindo origem e tipo da vulnerabilidade."""
    global attached_evidence

    dados = coletar_valores(widgets_dict)      

    if not dados:
        messagebox.showwarning("Atenção", "Nenhum campo preenchido.")
        return

    if not origem:
        messagebox.showwarning("Atenção", "Selecione a origem da vulnerabilidade.")
        return

    if not tipo_vuln:
        messagebox.showwarning("Atenção", "Selecione o tipo de vulnerabilidade.")
        return
    
    if any(valor.strip() == "" for valor in dados.values()):
        messagebox.showwarning("Validação", "Preencha todos os dados da Justificativa.")
        return    


    # Adiciona campos fixos
    dados_final = {
        "Origem": origem,
        "Tipo de Vulnerabilidade": tipo_vuln,
    }
    dados_final.update(dados)
    dados_final["Evidência"] = attached_evidence[:] if attached_evidence else []

    lista_justificativa.insert(tk.END, str(dados_final))
    attached_evidence = []
    messagebox.showinfo("Sucesso", f"Justificativa de {tipo_vuln} ({origem}) adicionada ✅")
