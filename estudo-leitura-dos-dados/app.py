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


# Cria o xlsx de acordo com csv passado por parametro e adiciona o dicionario
def createXlsx(csv):
    dicionary = [{'tag': tag, 'descricao': descricao}
                 for tag, descricao in zip(dicionaryTags, dicionaryTypes)]

    df_dict = pd.DataFrame(csv)
    df_dicionary = pd.DataFrame(dicionary)

    # Salve o DataFrame do dicionário em uma planilha específica dentro do arquivo CSV
    with pd.ExcelWriter('analise_pobreza_brasil.xlsx', engine='openpyxl') as writer:
        df_dict.to_excel(writer, sheet_name='Dados', index=False)
        df_dicionary.to_excel(writer, sheet_name='Dicionario', index=False)

    return


# calcula a porcentagem de pessoas pobre, dividindo a quantidade de pessoas pobre/ total de pessoas
def calculatePoorPercentage(csv):
    percentage_pes_poor = []

    for _, row in csv.iterrows():
        poor_percentage = (row['qtd_pes_pobres'] / row['qtd_pes']) * 100
        percentage_pes_poor.append(poor_percentage)

    return percentage_pes_poor


# calcula a porcentagem de pessoas vulneráveis, dividindo a quantidade de pessoas vulneráveis/ total de pessoas
def calculateVulnerablePercentage(csv):
    percentage_pes_vulnerable = []

    for _, row in csv.iterrows():
        vulnerable_percentage = (
            row['qtd_pes_vulneraveis'] / row['qtd_pes']) * 100
        percentage_pes_vulnerable.append(vulnerable_percentage)

    return percentage_pes_vulnerable

#calcula a media de renda média para região norte
def calculateAverageRevenueNorteRegion(csv):

    database_filter_norte_region = csv[csv['cod_regiao'] == regionTags[0]]

    avarage_revenue_norte_region = database_filter_norte_region['num_renda'].mean()

    return avarage_revenue_norte_region

#calcula a media de renda média para região nordeste
def calculateAverageRevenueNordesteRegion(csv):

    database_filter_nordeste_region = csv[csv['cod_regiao'] == regionTags[1]]

    avarage_revenue_nordeste_region = database_filter_nordeste_region['num_renda'].mean()

    return avarage_revenue_nordeste_region

# calcula a media de renda média para região sudeste
def calculateAverageRevenueSudesteRegion(csv):

    database_filter_sudeste_region = csv[csv['cod_regiao'] == regionTags[2]]

    avarage_revenue_sudeste_region = database_filter_sudeste_region['num_renda'].mean()

    return avarage_revenue_sudeste_region

# calcula a media de renda média para região sul
def calculateAverageRevenueSulRegion(csv):

    database_filter_sul_region = csv[csv['cod_regiao'] == regionTags[3]]

    avarage_revenue_sul_region = database_filter_sul_region['num_renda'].mean()

    return avarage_revenue_sul_region

# calcula a media de renda média para região Centro Oeste
def calculateAverageRevenueCentroOesteRegion(csv):

    database_filter_centro_oeste_region = csv[csv['cod_regiao'] == regionTags[4]]

    avarage_revenue_centro_oeste_region = database_filter_centro_oeste_region['num_renda'].mean()

    return avarage_revenue_centro_oeste_region



# Inicio das execuções

csv_data = pd.read_csv("MunicipioBrasil_20230102.csv")
csv_data_filtered = csv_data[dicionaryTags]  # CSV a ser manipulado

csv_data_filtered['percent_pes_pobres'] = calculatePoorPercentage(csv_data_filtered)

csv_data_filtered['percent_pes_vulneraveis'] = calculateVulnerablePercentage(
    csv_data_filtered)

csv_data_filtered['avarage_revenue_norte'] = calculateAverageRevenueNorteRegion(csv_data_filtered)

csv_data_filtered['avarage_revenue_nordeste'] = calculateAverageRevenueNordesteRegion(csv_data_filtered)

csv_data_filtered['avarage_revenue_sudeste'] = calculateAverageRevenueSudesteRegion(csv_data_filtered)

csv_data_filtered['avarage_revenue_sul'] = calculateAverageRevenueSulRegion(csv_data_filtered)

csv_data_filtered['avarage_revenue_centro_oeste'] = calculateAverageRevenueCentroOesteRegion(csv_data_filtered)

print(csv_data_filtered)


############
# TODO Criar uma nova aba para análise de dados por região
data_frame_regions = pd.DataFrame()

#############
# TODO falta calcular a media salarial por regiao.
data_frame_regions_tags = [
    'cod_regiao',
    'qtd_total_pes',
    'qtd_total_pes_pobre',
    'qtd_total_pes_vulneravel',
    'percent_pes_pobres',
    'percent_pes_vulneraveis',
]



# TODO falta calcular a media salarial por regiao.
# TODO falta calcular a porcentagem de pessoas pobres, comparada ao total de pessoas por região.
# TODO falta calcular a porcentagem de pessoas vulneráveis, comparada ao total de pessoas por região.

# createXlsx(csv_data_filtered)
