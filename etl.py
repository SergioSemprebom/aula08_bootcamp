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

# DICA DE MILHOES -> se quiser ficar testanto as FUNCTIONS
# Funçao extrair_dados'''
'''if __name__ == "__main__":
    pasta = "pasta"
    print(extrair_dados(path=pasta))'''

if __name__ == "__main__":
    pasta_argumento = "data"
    data_frame = extrair_dados_e_consolidar(path=pasta_argumento)
    print(calcular_kpi_de_total_de_vendas(data_frame))



    