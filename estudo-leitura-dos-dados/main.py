import pandas as pd

df = pd.read_csv('../MunicipioBrasil2.csv', encoding="LATIN-1", sep=",")

data = pd.DataFrame(df, columns= ['nom_mun', 'cod_regiao', 'num_renda', 'qtd_pes', 'qtd_pes_pobres', 'qtd_pes_vulneraveis', 'qtd_pes_pob_vul'])

filteredByRegion = data.loc[data['cod_regiao'] == 1]

print(filteredByRegion['num_renda'])

numRendaByRegion = pd.to_numeric(filteredByRegion["num_renda"], errors= 'coerce')

# print(numRendaByRegion)

# print("media", numRendaByRegion.mean())