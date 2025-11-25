# --- Conteúdo de src/revops_utils.py ---
import pandas as pd
from pathlib import Path

def encontrar_caminho_raiz(nome_pasta_chave: str = 'data') -> Path:
    
    caminho_atual = Path.cwd()
    for _ in range(5): # Limita a busca para evitar lentidão
        if (caminho_atual / nome_pasta_chave).exists():
            return caminho_atual
        caminho_atual = caminho_atual.parent
        if caminho_atual.parent == caminho_atual:
            break
            
    raise FileNotFoundError(f"Não foi possível encontrar a Raiz do Projeto (pasta '{nome_pasta_chave}' ausente).")

def carregar_dados_brutos_excel():


    try:
        raiz_projeto = encontrar_caminho_raiz()
        caminho_arquivo = raiz_projeto / 'data' / 'db_case_sales_ops.xlsx'
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Erro no caminho: Verifique a estrutura das pastas. Detalhe: {e}") from e
        
    print(f"✅ Raiz do projeto identificada em: {raiz_projeto.resolve()}")

    if not caminho_arquivo.exists():
        raise FileNotFoundError(f"Arquivo Excel não encontrado em: {caminho_arquivo.resolve()}")

    # 2. Carregamento do Excel
    print(f"Buscando dados em: {caminho_arquivo.resolve()}")
    xls = pd.ExcelFile(caminho_arquivo)
    
    # 3. Mapeia e Retorna os DataFrames
    dataframes = {
        'df_leads_bruto': pd.read_excel(xls, sheet_name='lead'),
        'df_visitas_bruto': pd.read_excel(xls, sheet_name='visitas'),
        'df_contratos_bruto': pd.read_excel(xls, sheet_name='contratos'),
        'df_geral_bruto': pd.read_excel(xls, sheet_name='geral')
    }
    
    print(f"✅ Sucesso! {len(dataframes)} DataFrames carregados.")
    return dataframes