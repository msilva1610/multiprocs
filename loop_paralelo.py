# artigo: https://superfastpython.com/multiprocessing-for-loop/

import itertools
import time
import multiprocessing 

from multiprocessing import Process

lista_primos = []

def calculadezenasPrimos(volante):
    # arrPrimos = []
    p = 0
    for numero in apostas[volante]:
        divisores = 0
        for divisor in range(1, numero):
            if numero % divisor == 0:
                divisores = divisores + 1
                if divisores > 1:
                    break
        if divisores > 1:
            pass
            # print("{} não é primo".format(numero))
        else:
            p += 1
    if p > 1:
        obj = {'id_aposta': volante, 'aposta': apostas[volante], 'qtdes_primos':p}
        lista_primos.append(obj)


def calculaApostas(nunDezenas):
    # volante = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
    # volante = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
    volante = list(range(1,31))
    apostas = []
    apostas = list(itertools.combinations(volante, nunDezenas))
    return apostas

apostas = calculaApostas(6)
if __name__ == '__main__':
    tipo = 2

    start = time.time()

    ids_apostas_list = range(1,len(apostas))

    if tipo == 1:
        for aposta_id in ids_apostas_list:
            calculadezenasPrimos(aposta_id)
        print(len(lista_primos))

    elif tipo == 2:
        processos = []
        # processes = [Process(target=task, args=(i,)) for i in range(20)]        
        for aposta_id in ids_apostas_list:
            processos.append(Process(target=calculadezenasPrimos, args=(aposta_id,)))
        
        for processo in processos:
            processo.start()

        for processo in processos:
            processo.join()

        print(len(lista_primos))
        # terminando com exceção: OSError: [Errno 23] Too many open files in system

    end = time.time()

    print(f'tempo: {end-start}')    