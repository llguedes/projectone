#%%
import pandas as pd
import sys; sys.path
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams['figure.figsize'] = (16,8)

print("Voce pode consultar o codigo da serie aqui:\n https://www3.bcb.gov.br/sgspub/localizarseries/localizarSeries.do?method=prepararTelaLocalizarSeries \n")
cod_bcb = input("Entre com o codigo da serie: ")
cod = int(cod_bcb)

def consulta_bc(cod):
    url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json'.format(cod)
    df = pd.read_json(url)
    df['data'] = pd.to_datetime(df['data'], dayfirst=True)
    df.set_index('data', inplace=True)
    return df

serie = consulta_bc(cod)
plt.plot(serie)
plt.show()







# %%
