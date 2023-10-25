import pandas as pd


def convertXlsxToCsv(xlsxName):
    read_file = pd.read_excel(xlsxName)

    read_file.to_csv("MunicipioBrasil_20230102.csv",
                     index=None,
                     header=True)

    return pd.DataFrame(pd.read_csv("MunicipioBrasil_20230102.csv"))


def convertCsvToXlsx(csvName):
    read_file = pd.read_csv(csvName)

    xlsxName = csvName.replace('.csv', '.xlsx')

    read_file.to_excel(xlsxName, index=None, header=True)

    return pd.read_excel(xlsxName)
