import pandas as pd
import os
import glob
# uma funcao de extract que le e consolida os json


def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    print(df_list)
    return df_total

# uma funcao que transforma
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df['Total'] = df["Quantidade"] * df["Venda"]
    return df

# uma funcao que da load em csv ou parquet

def carregar_dados(df: pd.DataFrame, format_saida: list):
    """
    parametro que vai ser ou "csv" ou "parquet" ou "os dois"
    """
    for formato in format_saida:
        if formato == "csv":
            df.to_csv("dados.csv", index=False)
        if formato == "parquet":
            df.to_parquet("dados.parquet", index=False)

def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, formato_de_saida: list):
    data_frame = extrair_dados_e_consolidar(pasta)
    data_frame_calculando = calcular_kpi_de_total_de_vendas(data_frame)
    formato_de_saida: list = ["csv", "parquet"]
    carregar_dados(data_frame_calculando, formato_de_saida)
    