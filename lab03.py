# link:https://github.com/andersonrocha0/tpa/blob/main/io_bound.py
# testes de processamento paralelo funcionou com sucesso. data:31/12/2023
import itertools
import time
import multiprocessing 
from multiprocessing import Pool, cpu_count

import pandas as pd
import numpy as np



def ret_dezenas(d1,d2,d3,d4,d5,d6):
    return [d1,d2,d3,d4,d5,d6]


def GeraCombinacoes(dezenasSorteios, numDezenas):
    return itertools.combinations(dezenasSorteios,numDezenas)


start = time.time()

sorteios_df = pd.read_excel('Mega-Sena.xlsx', parse_dates=['Data do Sorteio'])
sorteios_df.fillna('', inplace=True)
sorteios_df.replace('\n',' ', regex=True, inplace=True)
colunas = ['Bola1','Bola2','Bola3','Bola4','Bola5','Bola6']
dez_sorteadas_df  = sorteios_df[colunas]
dez_sorteadas_df['dezenas'] = dez_sorteadas_df.apply(
    lambda x:ret_dezenas(x['Bola1'],x['Bola2'],x['Bola3'],x['Bola4'],x['Bola5'],x['Bola6'],), axis=1
    )

# print(dez_sorteadas_df.head(1))

def gera_lista_tqq(df, q):
    lista_tqq = []
    for i in df.itertuples():
        dezenas = i[7]
        for comb in GeraCombinacoes(dezenas, q):
            d = list(comb)
            d.sort()
            lista_tqq.append(d)
    return lista_tqq

ternos = gera_lista_tqq(dez_sorteadas_df,3)

def calculaApostas(nunDezenas):
    volante = list(range(1,61))
    apostas = []
    apostas = list(itertools.combinations(volante, nunDezenas))
    return apostas


def calcula_algo(lista):
    qtde = 0
    for terno in ternos: 
        qtde = (len((set(terno) & set(lista))))
    return qtde


if __name__ == '__main__':
    # start = time.time()
    cores = cpu_count()

    lista_apostas = calculaApostas(6)

    pool = Pool(cores)
    
    lista_calculada = pool.map(calcula_algo, lista_apostas)

    df_sorteios_ternos = pd.DataFrame(lista_calculada)
    df_sorteios_ternos.to_csv('df_sorteios_ternos.csv', index=False)

    end = time.time()

    # print(f'tempo total: {end-start} - cpus: {cores} len: {len(lista_calculada)} ternos:{len(ternos)}')
    print(f'tempo total: {end-start} \ncpus: {cores} \nternos:{len(ternos)} \nlistaCalculada:{len(lista_calculada)}')
    # tempo total: 32.955262899398804 - cpus: 10 len: 50063860 ternos:10
