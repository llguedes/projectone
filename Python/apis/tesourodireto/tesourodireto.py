import pandas as pd
#pd.set_option("display.max_colwidth", 150, "display.min_rows", 20)

#import numpy as np

import matplotlib as plt
#matplotlib.style.use('seaborn-darkgrid')
plt.rcParams['figure.figsize'] = (10,5)

import matplotlib.pyplot as plt
#import plotly.graph_objects as go
#import plotly.express as px

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
 
menu = input("Escolha uma opcao:\n [1] - Titulos\n [2] - Vendas\n [3] - Recompras\n Opcao: ")

def titulos_tdireto():
    url = 'https://www.tesourotransparente.gov.br/ckan/dataset/df56aa42-484a-4a59-8184-7676580c81e3/resource/796d2059-14e9-44e3-80c9-2d9e30b405c1/download/PrecoTaxaTesouroDireto.csv'
    df  = pd.read_csv(url, sep=';', decimal=',')
    df['Data Vencimento'] = pd.to_datetime(df['Data Vencimento'], dayfirst=True)
    df['Data Base'] = pd.to_datetime(df['Data Base'], dayfirst=True)
    multi_indice = pd.MultiIndex.from_frame(df.iloc[:, :3])
    df = df.set_index(multi_indice).iloc[: , 3:]  
    return df

def vendas_tdireto():
    url = 'https://www.tesourotransparente.gov.br/ckan/dataset/f0468ecc-ae97-4287-89c2-6d8139fb4343/resource/e5f90e3a-8f8d-4895-9c56-4bb2f7877920/download/VendasTesouroDireto.csv'
    df  = pd.read_csv(url, sep=';', decimal=',')
    df['Vencimento do Titulo'] = pd.to_datetime(df['Vencimento do Titulo'], dayfirst=True)
    df['Data Venda'] = pd.to_datetime(df['Data Venda'], dayfirst=True)
    multi_indice = pd.MultiIndex.from_frame(df.iloc[:, :3])
    df = df.set_index(multi_indice).iloc[: , 3:]  
    return df

def recompras_tdireto():
    url = 'https://www.tesourotransparente.gov.br/ckan/dataset/f30db6e4-6123-416c-b094-be8dfc823601/resource/30c2b3f5-6edd-499a-8514-062bfda0f61a/download/RecomprasTesouroDireto.csv'
    df  = pd.read_csv(url, sep=';', decimal=',')
    df['Vencimento do Titulo'] = pd.to_datetime(df['Vencimento do Titulo'], dayfirst=True)
    df['Data Resgate'] = pd.to_datetime(df['Data Resgate'], dayfirst=True)
    multi_indice = pd.MultiIndex.from_frame(df.iloc[:, :3])
    df = df.set_index(multi_indice).iloc[: , 3:]  
    return df

def plotframe():
        
    titulos.sort_index(inplace=True)    
    #print(titulos)
    titulos.plot()
    plt.xticks(
        rotation=45, 
        horizontalalignment='right',
        fontweight='light'
    )    
    plt.show()

if (menu == 1):
    titulos = titulos_tdireto()
    plotframe()
    
elif (menu == 2):
    titulos = vendas_tdireto()
    plotframe()
    
elif (menu == 3):
    titulos = recompras_tdireto()
    plotframe()
else:
    print("Valor nao identificado")




