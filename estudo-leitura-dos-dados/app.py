import pandas as pd

dicionaryTags = [
    'cod_regiao',
    'qtd_pes',
    'qtd_pes_pobres',
    'qtd_pes_vulneraveis',
    'qtd_pes_pob_vul',
    'num_renda',
]

dicionaryTypes = [
    'Código da Grande Região',
    'Número de pessoas',
    'Númeo de pessoas pobres',
    'Número de pessoas vulneráveis',
    'Número de pessoas pobres ou vulneráveis',
    'Renda média (R$)'
]

regionTags = [1, 2, 3, 4, 5]

regionTypes = [
    'Norte',
    'Nordeste',
    'Sudeste',
    'Sul',
    'Centro-Oeste'
]

data_frame_regions_tags = [
    'avg_revenue_norte',
    'avg_revenue_nordeste',
    'avg_revenue_sudeste',
    'avg_revenue_sul',
    'avg_revenue_centro_oeste'
]

data_frame_regions_types = [
    'Renda média do Norte',
    'Renda média do Nordeste',
    'Renda média do Sudeste',
    'Renda média do Sul',
    'Renda média do Centro Oeste'
]


# Cria o xlsx de acordo com csv passado por parametro e adiciona o dicionario
def createXlsx(csv, region):
    dicionary = [{'tag': tag, 'descricao': descricao}
                 for tag, descricao in zip(dicionaryTags, dicionaryTypes)]

    df_dict = pd.DataFrame(csv)
    df_dicionary = pd.DataFrame(dicionary)
    df_region = pd.DataFrame(region)

    # Salve o DataFrame do dicionário em uma planilha específica dentro do arquivo CSV
    with pd.ExcelWriter('analise_pobreza_brasil.xlsx', engine='openpyxl') as writer:
        df_dict.to_excel(writer, sheet_name='Dados', index=False)
        df_dicionary.to_excel(writer, sheet_name='Dicionario', index=False)
        df_region.to_excel(writer, sheet_name='Análise', index=False)
    return


# calcula a porcentagem de pessoas vulneráveis ou pobres, dividindo a quantidade de pessoas vulneráveis ou pobres/ total de pessoas
def calculatePesPercentage(csv, regionTag: int, columNameFiltered: str):
    database_filter = csv[csv['cod_regiao'] == regionTag]

    total_pes = database_filter['qtd_pes'].sum()
    colum_name = database_filter[columNameFiltered].sum()

    return (colum_name / total_pes) * 100


# Calcula a renda media por regiao
def calculateAverageRevenue(csv, regionTag: int):
    database_filter = csv[csv['cod_regiao'] == regionTag]
    avarage_revenue = database_filter['num_renda'].mean()
    return avarage_revenue

# Calcula o total de pessoas de uma coluna, filtrada por regiao


def calculateTotalPes(csv, regionTag: int, columNameFiltered: str):
    filter_region = csv[csv['cod_regiao'] == regionTag]
    return filter_region[columNameFiltered].sum()

# Gera um data frame com os resultados


def executeDataFrameResults(csv):
    data_frame_regions = pd.DataFrame()

    for region in regionTags:
        data = {
            'cod_regiao': region,
            'qtd_total_pes': calculateTotalPes(csv, region, 'qtd_pes'),
            'qtd_total_pes_pobre': calculateTotalPes(csv, region, 'qtd_pes_pobres'),
            'qtd_total_pes_vulneravel': calculateTotalPes(csv, region, 'qtd_pes_vulneraveis'),
            'percent_pes_pobre': calculatePesPercentage(csv, region, 'qtd_pes_pobres'),
            'percent_pes_vulneraveis': calculatePesPercentage(csv, region, 'qtd_pes_vulneraveis'),
            'num_renda': calculateAverageRevenue(csv, region)
        }

        new_row = pd.DataFrame(data, index=[0])

        data_frame_regions = pd.concat(
            [data_frame_regions, new_row], ignore_index=True)

    return data_frame_regions


#############
# Filtra os dados
csv_data = pd.read_csv("MunicipioBrasil_20230102.csv")
csv_data_filtered = csv_data[dicionaryTags]
df_results = executeDataFrameResults(csv_data_filtered)

createXlsx(csv_data_filtered, df_results)
