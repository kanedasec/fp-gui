### Criado para converter listas de txt em listas de python

def txt_para_lista(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            return [linha.strip() for linha in arquivo if linha.strip()]
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return []

def salvar_lista_em_arquivo(lista, caminho_saida):
    try:
        with open(caminho_saida, 'w', encoding='utf-8') as f:
            f.write("SDU_DATA = [\n")
            for i, item in enumerate(lista):
                separador = "," if i < len(lista) - 1 else ""
                f.write(f'    "{item}"{separador}\n')
            f.write("]\n")
        print(f"Arquivo '{caminho_saida}' gerado com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")


# Execução
lista = txt_para_lista("utils/vuln_data/lista.txt")
salvar_lista_em_arquivo(lista, "utils/vuln_data/sdu_data.py")