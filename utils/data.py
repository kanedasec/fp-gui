from utils import vuln_data

SESSAO_AUTENTICADA = ["Sim", "Não"]

RISCO = ["Vulnerabilidade não se aplica", "Vulnerabilidade Mitigado", "Auxílio para correção", "Falso Positivo Confirmado", "Dependência Externa ou de Terceiro"]


CRITICIDADE = ["informativo", "baixa", "média", "alta", "crítica"]

AMBIENTE = ["Internet", "Intranet", "Ambos"]

perguntas = [
    "Nome da Aplicação\n na Esteira:",
    "Esteira:",
    "Branch:",
    "Aplicação faz uso\n de sessão autenticada?",
    "Aplicação é exposta\n em qual ambiente?",
    "Qual o tipo de Vulnerabilidade?",
    "Justificativa:",
    "Criticidade:",
    "Quantidade:",
    "Apontamento Mitigado",
    "Não existe risco",
    "Items Justificados:",
    ]


ORIGENS = {
    "SAST": {
        "dados_aplicacao": [
            {"label": "Nome da Aplicação", "type": "entry"},
            {"label": "Esteira", "type": "entry"},
            {"label": "Branch", "type": "entry"},
            {"label": "Sessão Autenticada?", "type": "combobox", "values": SESSAO_AUTENTICADA},
            {"label": "Ambiente", "type": "combobox", "values": AMBIENTE},
        ],
        "vulnerabilidades": vuln_data.SAST_DATA,
        "formulario": [
            {"label": "Criticidade", "type": "combobox", "values": CRITICIDADE},
            {"label": "Quantidade de Apontamentos", "type": "entry"},
            {"label": "Estado da Vulnerabilidade", "type": "combobox", "values": RISCO},
            {"label": "Justificativa", "type": "text"},
        ],
    },

    "DAST": {
        "dados_aplicacao": [
            {"label": "Nome da Aplicação", "type": "entry"},
            {"label": "Esteira", "type": "entry"},
            {"label": "Branch", "type": "entry"},
            {"label": "Sessão Autenticada?", "type": "combobox", "values": SESSAO_AUTENTICADA},
            {"label": "Ambiente", "type": "combobox", "values": AMBIENTE},
        ],
        "vulnerabilidades": vuln_data.SAST_DATA,
        "formulario": [
            {"label": "Criticidade", "type": "combobox", "values": CRITICIDADE},
            {"label": "Quantidade de Apontamentos", "type": "entry"},
            {"label": "Estado da Vulnerabilidade", "type": "combobox", "values": RISCO},
            {"label": "Justificativa", "type": "text"},
        ],
    },

    "SDU": {
        "dados_aplicacao": [
            {"label": "Nome do Serviço", "type": "entry"},
            {"label": "Url", "type": "entry"},
            {"label": "Ambiente", "type": "combobox", "values": AMBIENTE},
        ],
        "vulnerabilidades": vuln_data.SDU_DATA,
        "formulario": [
            {"label": "IDs das Vulnerabilidades", "type": "entry"},
            {"label": "Criticidade", "type": "combobox", "values": CRITICIDADE},
            {"label": "Estado da Vulnerabilidade", "type": "combobox", "values": ["Mitigada", "Erradicada"]},
            {"label": "Justificativa técnica", "type": "text"},
        ],
    },

    "BSV": {
        "dados_aplicacao": [
            {"label": "Nome do Serviço", "type": "entry"},
            {"label": "Url", "type": "entry"},
            {"label": "Ambiente", "type": "combobox", "values": AMBIENTE},
        ],
        "vulnerabilidades": vuln_data.BSV_DATA,
        "formulario": [
            {"label": "IDs das Vulnerabilidades", "type": "entry"},
            {"label": "Criticidade", "type": "combobox", "values": CRITICIDADE},
            {"label": "Estado da Vulnerabilidade", "type": "combobox", "values": ["Mitigada", "Erradicada"]},
            {"label": "Justificativa técnica", "type": "text"},
        ],
    }
}
