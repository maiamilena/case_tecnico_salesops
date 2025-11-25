"""

Este script:
- detecta automaticamente o caminho correto do arquivo .xlsx
- valida a existência do arquivo
- carrega o dataset em um DataFrame
- cria diretório processed/ se necessário
- deixa tudo pronto para uso em qualquer máquina
"""

import pandas as pd
from pathlib import Path


def load_dataset(file_name: str = "db_case_sales_ops.xlsx"):
    """
    Carrega o dataset do case de RevOps de forma portátil.
    
    Args:
        file_name (str): Nome do arquivo dentro da pasta /data.
        
    Returns:
        pd.DataFrame: DataFrame carregado.
    """

    # Caminho raiz do projeto (onde está o README.md)
    root = Path(__file__).resolve().parent.parent

    data_path = root / "data" / file_name

    if not data_path.exists():
        raise FileNotFoundError(
            f"❌ Arquivo não encontrado em {data_path}\n"
            "Verifique se o arquivo está na pasta /data."
        )

    print(f"📁 Carregando arquivo: {data_path}")

    df = pd.read_excel(data_path)

    print("✅ Dataset carregado com sucesso!")
    print(f"🔹 Linhas: {df.shape[0]} | Colunas: {df.shape[1]}")

    # Garante o diretório processed/
    processed_path = root / "processed"
    processed_path.mkdir(exist_ok=True)

    return df


if __name__ == "__main__":
    df = load_dataset()

    print("\n📊 Primeiras 5 linhas:")
    print(df.head())
