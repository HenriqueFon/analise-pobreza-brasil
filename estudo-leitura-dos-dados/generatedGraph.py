import pandas as pd
import matplotlib.pyplot as plt
import locale

csv = pd.read_csv("analise_pobreza_brasil.csv")


def createAverageSalaryGraph():
    regionTypes = [
        'Norte',
        'Nordeste',
        'Sudeste',
        'Sul',
        'Centro-Oeste'
    ]

    plt.title('Renda média por Região do Brasil')
    plt.xlabel('Região')
    plt.ylabel('Renda Média R$')
    plt.bar(regionTypes, csv['num_renda'], alpha=0.7,
            capsize=5)
    plt.xticks(regionTypes, ['Norte', 'Nordeste',
               'Sudeste', 'Sul', 'Centro-Oeste'])
    plt.legend()
    plt.show()


def createCircleGraph(columName: str, title: str):
    regionTypes = [
        'Norte',
        'Nordeste',
        'Sudeste',
        'Sul',
        'Centro-Oeste'
    ]

    labels = regionTypes
    sizes = csv[columName]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'blue']
    explode = (0, 0.1, 0, 0, 0)

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title(title)
    plt.axis('equal')
    plt.show()


def createCircleTotalGraph(columName: str, title: str):
    regionTypes = [
        'Norte',
        'Nordeste',
        'Sudeste',
        'Sul',
        'Centro-Oeste'
    ]

    labels = regionTypes
    sizes = csv[columName]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'blue']
    explode = (0, 0, 0.1, 0, 0)

    # Defina o locale para formatar números
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    # Formate os valores com separadores de milhar e um ponto decimal
    formatted_sizes = [locale.format_string(
        '%.0f', size, grouping=True) for size in sizes]

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title(title)
    plt.axis('equal')

    # Adicione uma legenda personalizada com os valores formatados
    plt.legend(labels=[f'{label}: {value}' for label,
               value in zip(labels, formatted_sizes)])

    plt.show()


def createDevioPadrao():
    # Calcular a média e o desvio padrão da quantidade de pessoas pobres por região
    media_por_regiao = csv['qtd_total_pes_pobre'].groupby(
        csv['cod_regiao']).mean()
    desvio_padrao_por_regiao = csv['qtd_total_pes_pobre'].groupby(
        csv['cod_regiao']).std()

    # Preparar os dados para o gráfico
    regioes = media_por_regiao.index
    media = media_por_regiao.values
    desvio_padrao = desvio_padrao_por_regiao.values

    # Criar um gráfico de colunas com barras de erro
    plt.bar(regioes, media, alpha=0.7, yerr=desvio_padrao,
            capsize=5, label='Média com Desvio Padrão')
    plt.xlabel('Região')
    plt.ylabel('Média de Pessoas Pobres')
    plt.title('Média de Pessoas Pobres por Região com Desvio Padrão')
    plt.xticks(regioes, ['Norte', 'Nordeste',
               'Sudeste', 'Sul', 'Centro-Oeste'])
    plt.legend()

    # Exibir o gráfico
    plt.show()


createCircleTotalGraph('qtd_total_pes',
                       'Total de Pessoas Por Região no Brasil')
