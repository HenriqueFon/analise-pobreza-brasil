import pandas as pd


def createXlsx(data):
    dicionary = [{'tag': tag, 'descricao': descricao}
                 for tag, descricao in zip(dicionaryTags, dicionaryTypes)]

    df_dict = pd.DataFrame(data)
    df_dicionary = pd.DataFrame(dicionary)

    # Salve o DataFrame do dicionário em uma planilha específica dentro do arquivo CSV
    with pd.ExcelWriter('analise_pobreza_brasil.xlsx', engine='openpyxl') as writer:
        df_dict.to_excel(writer, sheet_name='Dados', index=False)
        df_dicionary.to_excel(writer, sheet_name='Dicionario', index=False)

    return


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

createXlsx(csv)
