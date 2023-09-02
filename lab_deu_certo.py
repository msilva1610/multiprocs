
from multiprocessing import Pool, cpu_count
import numpy as np
import itertools
import pandas as pd
from random import sample
import multiprocessing 
from multiprocessing.shared_memory import ShareableList
# function to be applied for each element
from time import perf_counter

t1 = perf_counter()

def pool_initializer(TERNOS):
    global lista_ternos
    lista_ternos = TERNOS

def conta_ternos(dezena):
    global lista_ternos
    qtde = 0
    tot = 0
    for terno in lista_ternos:
        qtde = (len((list((set(terno) & set(dezena))))))
        if qtde == 3:
            tot += 1
    return tot


if __name__ == "__main__":
    print('passei aqui')

    numeros = list(range(1,61))
    combinacoes = itertools.combinations(numeros,6)
    apostas = (list(combinacoes))    
    ternos_sorteados = []
    for aposta in sample(apostas,50000):
        for terno in itertools.combinations(aposta,3):
            ternos_sorteados.append(terno)  

    dezenas = apostas
    # dezenas = [(19, 23, 32, 43, 46, 59),(9, 14, 22, 19, 46, 59),(9, 14, 23, 33, 37, 50)]
    ternos_da_aposta = ternos_sorteados

    pool = Pool(
        processes=cpu_count(), 
        initializer=pool_initializer, 
        initargs=([ternos_da_aposta]))
    res = pool.map(conta_ternos, dezenas)
    # print(res)
    print(perf_counter() -t1)
