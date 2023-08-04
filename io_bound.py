# link:https://github.com/andersonrocha0/tpa/blob/main/io_bound.py

import requests
import time
import sys
from enum import Enum

import asyncio
import aiohttp


async def get_cervejaria_async(id_c, session):
    async with session.get(f'https://api.openbrewerydb.org/breweries/{id_c}') as response:
        print(await response.json())


async def processar_async(ids):
    coros = []
    async with aiohttp.ClientSession() as session:
        for id_c in ids:
            coros.append(get_cervejaria_async(id_c, session))

        await asyncio.gather(*coros)

class TipoExecucao(Enum):
    UM_PROCESSO = 1
    VARIOS_PROCESSOS = 2
    VARIAS_THREADS = 3
    ASYNCIO_COM_LIB_HTTP = 4
    ASYNCIO_MANUAL = 5


def get_cervejaria(id_c):
    r = requests.get(f'https://api.openbrewerydb.org/breweries/{id_c}')
    if r.status_code == 200:
        print(r.json())


def get_ids_cervejarias():
    r = requests.get('https://api.openbrewerydb.org/breweries')
    if r.status_code == 200:
        return [r['id'] for r in r.json()]

if __name__ == '__main__':
    started = time.time()

    ids_cervejarias = get_ids_cervejarias()
    # print(ids_cervejarias)

    tipo_execucao = TipoExecucao.ASYNCIO_COM_LIB_HTTP

    if TipoExecucao.UM_PROCESSO == tipo_execucao:
        # Usando somente um processo
        for id_cervejaria in ids_cervejarias:
            get_cervejaria(id_cervejaria) 

    elif TipoExecucao.ASYNCIO_COM_LIB_HTTP == tipo_execucao:
        # Usando asyncio
        event_loop = asyncio.get_event_loop()
        tasks = []

        event_loop.run_until_complete(processar_async(ids_cervejarias))


    elapsed = time.time()
    print('Time taken :', elapsed - started)

    sys.exit(0)    

