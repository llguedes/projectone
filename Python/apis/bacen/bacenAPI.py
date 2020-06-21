import pandas as pd
import sys; sys.path
import seaborn as sns; sns.set()
import matploitlib.pyplot as plt

import matplotlib
matplotlib.rcParams['figure.figsize'] = (16,8)

cod_bcb = input("Entre com o codigo: ")

def consulta_bc(cod_bcb):
    url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json'.format(cod_bcb)
    df = pd.read_json(url)
    df['data'] = pd.to_datetime(df['data'], dayfirst=True)
    df.set_index('data', implace=True)
    return df





