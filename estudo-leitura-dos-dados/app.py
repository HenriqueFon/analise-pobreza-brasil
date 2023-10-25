import pandas as pd

csv = pd.read_csv("MunicipioBrasil_20230102.csv")

dicionaryTags = [
    'cod_regiao',
    'qtd_pes',
    'qtd_pes_pobres',
    'qtd_pes_vulneraveis',
    'qtd_pes_pob_vul'
]

dicionaryTypes = [
    'Código da Grande Região',
    'Número de pessoas',
    'Númeo de pessoas pobres',
    'Número de pessoas vulneráveis',
    'Número de pessoas pobres ou vulneráveis'
]


dicionary = [{'tag': tag, 'descricao': descricao}
             for tag, descricao in zip(dicionaryTags, dicionaryTypes)]

print(dicionary)

# Converta o dicionário em um DataFrame Pandas
df_dict = pd.DataFrame()

# Crie um DataFrame vazio que representará o restante do arquivo CSV
df_dicionary = pd.DataFrame(dicionary)

# Salve o DataFrame do dicionário em uma planilha específica dentro do arquivo CSV
with pd.ExcelWriter('dale.xlsx', engine='openpyxl') as writer:
    df_dict.to_excel(writer, sheet_name='xxx', index=False)
    df_dicionary.to_excel(writer, sheet_name='Dicionaty', index=False)
