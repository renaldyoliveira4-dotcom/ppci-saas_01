"""
NORMAS - Sistemas de Proteção Contra Incêndio Exigidos
Baseado na IT-01 do CBMBA (Tabela de Exigências)

INSTRUÇÕES PARA ATUALIZAÇÃO:
- Cada regra define condições para exigência de um sistema
- Adicione novas regras conforme revisão das ITs
- Use as funções auxiliares para verificar exigências
"""

from typing import Any

# Definição dos sistemas de proteção
SISTEMAS_PROTECAO = {
    "ACESSO_VIATURAS": {
        "codigo": "AV",
        "nome": "Acesso de viaturas na edificação",
        "it_referencia": "IT-06",
        "descricao": "Condições de acesso para viaturas do corpo de bombeiros",
    },
    "SEGURANCA_ESTRUTURAL": {
        "codigo": "SE",
        "nome": "Segurança estrutural contra incêndio",
        "it_referencia": "IT-08",
        "descricao": "Resistência ao fogo dos elementos estruturais e de compartimentação",
    },
    "COMPARTIMENTACAO": {
        "codigo": "CH/CV",
        "nome": "Compartimentação horizontal e vertical",
        "it_referencia": "IT-09",
        "descricao": "Compartimentação para conter a propagação do incêndio",
    },
    "CONTROLE_MATERIAIS": {
        "codigo": "CMAR",
        "nome": "Controle de materiais de acabamento e revestimento",
        "it_referencia": "IT-10",
        "descricao": "Características dos materiais de acabamento e revestimento",
    },
    "SAIDA_EMERGENCIA": {
        "codigo": "SAI",
        "nome": "Saídas de emergência",
        "it_referencia": "IT-11",
        "descricao": "Dimensionamento e disposição das saídas de emergência",
    },
    "ILUMINACAO_EMERGENCIA": {
        "codigo": "ILE",
        "nome": "Iluminação de emergência",
        "it_referencia": "IT-18",
        "descricao": "Sistema de iluminação de emergência para evacuação",
    },
    "SINALIZACAO_EMERGENCIA": {
        "codigo": "SNE",
        "nome": "Sinalização de emergência",
        "it_referencia": "IT-20",
        "descricao": "Sinalização de segurança contra incêndio e pânico",
    },
    "ALARME_INCENDIO": {
        "codigo": "ALM",
        "nome": "Alarme de incêndio",
        "it_referencia": "IT-19",
        "descricao": "Sistema de alarme para detecção e aviso de incêndio",
    },
    "DETECCAO_INCENDIO": {
        "codigo": "DET",
        "nome": "Detecção de incêndio",
        "it_referencia": "IT-19",
        "descricao": "Sistema de detecção automática de incêndio",
    },
    "EXTINTORES": {
        "codigo": "EXT",
        "nome": "Extintores de incêndio",
        "it_referencia": "IT-04",
        "descricao": "Proteção por extintores portáteis e sobre rodas",
    },
    "HIDRANTES": {
        "codigo": "HID",
        "nome": "Hidrantes e mangotinhos",
        "it_referencia": "IT-17",
        "descricao": "Sistema de hidrantes e mangotinhos para combate a incêndio",
    },
    "CHUVEIROS_AUTOMATICOS": {
        "codigo": "CHV",
        "nome": "Chuveiros automáticos (sprinklers)",
        "it_referencia": "IT-23",
        "descricao": "Sistema de chuveiros automáticos para extinção",
    },
    "GLP": {
        "codigo": "GLP",
        "nome": "Central de GLP",
        "it_referencia": "IT-28",
        "descricao": "Instalações de gás liquefeito de petróleo",
    },
    "PARA_RAIOS": {
        "codigo": "SPDA",
        "nome": "Sistema de proteção contra descargas atmosféricas",
        "it_referencia": "NBR 5419",
        "descricao": "Proteção contra raios (SPDA)",
    },
    "BRIGADA_INCENDIO": {
        "codigo": "BRG",
        "nome": "Brigada de incêndio",
        "it_referencia": "IT-12",
        "descricao": "Formação de brigada de incêndio",
    },
    "PLANO_EMERGENCIA": {
        "codigo": "PLE",
        "nome": "Plano de emergência contra incêndio",
        "it_referencia": "IT-16",
        "descricao": "Plano de emergência e procedimentos de evacuação",
    },
}

# Tabela simplificada de exigências por grupo/condição
# Formato: lista de regras com condições e sistemas exigidos
REGRAS_EXIGENCIA = [
    # Regras universais (para qualquer edificação)
    {
        "condicao": "TODAS",
        "descricao": "Exigências básicas para todas as edificações",
        "area_minima": 0,
        "altura_minima": 0,
        "sistemas": ["EXTINTORES", "SAIDA_EMERGENCIA", "ILUMINACAO_EMERGENCIA", "SINALIZACAO_EMERGENCIA"],
    },
    # Edificações acima de 700 m² (IT-17 CBMBA)
    {
        "condicao": "AREA_ACIMA_700",
        "descricao": "Exigências para edificações com área > 700 m²",
        "area_minima": 700,
        "altura_minima": 0,
        "sistemas": ["ALARME_INCENDIO", "HIDRANTES"],
    },
    # Edificações acima de 12m de altura
    {
        "condicao": "ALTURA_ACIMA_12",
        "descricao": "Exigências para edificações com altura > 12 m",
        "area_minima": 0,
        "altura_minima": 12,
        "sistemas": ["ALARME_INCENDIO", "SEGURANCA_ESTRUTURAL", "COMPARTIMENTACAO"],
    },
    # Edificações acima de 23m de altura
    {
        "condicao": "ALTURA_ACIMA_23",
        "descricao": "Exigências para edificações com altura > 23 m",
        "area_minima": 0,
        "altura_minima": 23,
        "sistemas": ["DETECCAO_INCENDIO", "BRIGADA_INCENDIO", "PLANO_EMERGENCIA"],
    },
    # Edificações acima de 30m de altura
    {
        "condicao": "ALTURA_ACIMA_30",
        "descricao": "Exigências para edificações com altura > 30 m",
        "area_minima": 0,
        "altura_minima": 30,
        "sistemas": ["CHUVEIROS_AUTOMATICOS"],
    },
    # Edificações acima de 5000 m²
    {
        "condicao": "AREA_ACIMA_5000",
        "descricao": "Exigências para edificações com área > 5.000 m²",
        "area_minima": 5000,
        "altura_minima": 0,
        "sistemas": ["ACESSO_VIATURAS", "BRIGADA_INCENDIO", "PLANO_EMERGENCIA"],
    },
    # Edificações de reunião de público (F)
    {
        "condicao": "REUNIAO_PUBLICO",
        "descricao": "Exigências adicionais para locais de reunião de público",
        "grupos": ["F"],
        "area_minima": 0,
        "altura_minima": 0,
        "sistemas": ["ALARME_INCENDIO", "BRIGADA_INCENDIO"],
    },
    # Edificações de saúde (H)
    {
        "condicao": "SAUDE",
        "descricao": "Exigências adicionais para serviços de saúde",
        "grupos": ["H"],
        "area_minima": 0,
        "altura_minima": 0,
        "sistemas": ["ALARME_INCENDIO", "DETECCAO_INCENDIO", "PLANO_EMERGENCIA"],
    },
    # Risco elevado
    {
        "condicao": "RISCO_ELEVADO",
        "descricao": "Exigências adicionais para risco elevado",
        "risco": "ELEVADO",
        "area_minima": 0,
        "altura_minima": 0,
        "sistemas": ["DETECCAO_INCENDIO", "BRIGADA_INCENDIO"],
    },
    # Com subsolo
    {
        "condicao": "COM_SUBSOLO",
        "descricao": "Exigências adicionais para edificações com subsolo",
        "possui_subsolo": True,
        "area_minima": 0,
        "altura_minima": 0,
        "sistemas": ["DETECCAO_INCENDIO"],
    },
]


def determinar_sistemas_exigidos(
    area_construida: float,
    altura: float,
    grupo: str,
    risco: str,
    possui_subsolo: bool = False,
) -> list[dict]:
    """
    Determina os sistemas de proteção exigidos para a edificação.
    Retorna lista de sistemas com suas referências normativas.
    """
    sistemas_ids = set()

    for regra in REGRAS_EXIGENCIA:
        aplicar = False

        if regra["condicao"] == "TODAS":
            aplicar = True
        elif regra["condicao"].startswith("AREA_ACIMA"):
            aplicar = area_construida > regra["area_minima"]
        elif regra["condicao"].startswith("ALTURA_ACIMA"):
            aplicar = altura > regra["altura_minima"]
        elif regra["condicao"] == "REUNIAO_PUBLICO":
            aplicar = grupo.upper() in regra.get("grupos", [])
        elif regra["condicao"] == "SAUDE":
            aplicar = grupo.upper() in regra.get("grupos", [])
        elif regra["condicao"] == "RISCO_ELEVADO":
            aplicar = risco.upper() == "ELEVADO"
        elif regra["condicao"] == "COM_SUBSOLO":
            aplicar = possui_subsolo

        if aplicar:
            for s in regra["sistemas"]:
                sistemas_ids.add(s)

    resultado = []
    for sid in sorted(sistemas_ids):
        info = SISTEMAS_PROTECAO.get(sid, {})
        resultado.append({
            "id": sid,
            "codigo": info.get("codigo", ""),
            "nome": info.get("nome", sid),
            "it_referencia": info.get("it_referencia", ""),
            "descricao": info.get("descricao", ""),
        })

    return resultado


def definir_tipo_processo(
    area_construida: float,
    altura: float,
    grupo: str,
    divisao: str,
    numero_pavimentos: int = 1,
    populacao: int = 0,
    risco: str = "LEVE",
    exige_hidrante: bool = False,
) -> dict:
    """
    Define se o processo é PTS (Processo Técnico Simplificado)
    ou Projeto Técnico completo.

    Baseado na IT-01/IT-42 do CBMBA, PTS exige TODAS as condições:
    - Área ≤ 750 m² E até 3 pavimentos, OU área ≤ 1.500 m² E altura ≤ 6 m
    - NÃO seja grupo F com população > 100
    - NÃO seja grupo H (saúde)
    - NÃO seja indústria I-2 ou I-3 (risco médio/alto)
    - NÃO seja depósito J-2 (carga média/alta)
    - NÃO seja explosivos (L-1, L-2, L-3)
    - NÃO exija sistema hidráulico (hidrantes/sprinklers)
    - NÃO tenha risco elevado de incêndio
    """
    motivos = []
    grupo_u = grupo.upper()
    divisao_u = divisao.upper()

    # Validação de área e pavimentos
    if area_construida > 1500:
        motivos.append(f"Área {area_construida} m² acima de 1.500 m²")
    elif area_construida > 750 and altura > 6:
        motivos.append(
            f"Área {area_construida} m² > 750 m² e altura {altura} m > 6 m"
        )

    if numero_pavimentos > 3:
        motivos.append(f"{numero_pavimentos} pavimentos (máximo 3 para PTS)")
    if altura > 12:
        motivos.append(f"Altura {altura} m acima de 12 m")

    # Grupos e divisões não-elegíveis
    if grupo_u == "H":
        motivos.append("Grupo H (serviços de saúde)")
    if grupo_u == "F" and populacao > 100:
        motivos.append(f"Grupo F com população {populacao} (> 100 pessoas)")
    if divisao_u in ("I-2", "I-3"):
        motivos.append(f"Divisão {divisao_u} (indústria risco médio/alto)")
    if divisao_u == "J-2":
        motivos.append("Depósito de carga média/alta (J-2)")
    if divisao_u in ("L-1", "L-2", "L-3"):
        motivos.append(f"Explosivos (divisão {divisao_u})")

    # Sistemas e risco
    if exige_hidrante:
        motivos.append("Exige sistema hidráulico de combate")
    if risco.upper() == "ELEVADO":
        motivos.append("Risco elevado de incêndio")

    if not motivos:
        return {
            "tipo": "PTS",
            "descricao": "Processo Técnico Simplificado",
            "justificativa": (
                f"Edificação com área {area_construida} m², altura {altura} m, "
                f"{numero_pavimentos} pavimento(s), grupo {grupo_u} atende todos "
                f"os requisitos da IT-01/IT-42 CBMBA para PTS"
            ),
            "norma_referencia": "IT-01 / IT-42 CBMBA",
        }

    return {
        "tipo": "PROJETO_TECNICO",
        "descricao": "Projeto Técnico Completo",
        "justificativa": "Não atende PTS pelos motivos: " + "; ".join(motivos),
        "norma_referencia": "IT-01 / IT-42 CBMBA",
    }
