# link:https://github.com/andersonrocha0/tpa/blob/main/io_bound.py
# testes de processamento paralelo funcionou com sucesso. data:31/12/2023
import itertools
import time
import multiprocessing 
from multiprocessing import Pool, cpu_count

manager = multiprocessing.Manager()
final_list = manager.list()


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
        final_list.append(obj)


def calculaApostas(nunDezenas):
    # volante = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
    # volante = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
    # volante = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    volante = list(range(1,31))
    apostas = []
    apostas = list(itertools.combinations(volante, nunDezenas))
    return apostas


apostas = calculaApostas(6)
if __name__ == '__main__':
    start = time.time()
    cores = cpu_count()

    ids_apostas_list = range(len(apostas))
    # Usando vários processos
    pool = Pool(cores)
    pool.map(calculadezenasPrimos, ids_apostas_list)

    print(f'Total de primos: {len(final_list)}')
    i = 0
    for item in final_list:
        i += 1
        if item['id_aposta'] == 5004:
            print(item)
    end = time.time()

    print(f'tempo: {end-start}')