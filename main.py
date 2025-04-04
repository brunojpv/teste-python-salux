from collections import OrderedDict
import pandas as pd
import asyncio
import aiohttp

print("\n==================== LRUCache ====================\n")

# LRUCache (Least Recently Used)
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Teste do LRUCache
cache = LRUCache(3)
cache.put(1, 'A')
cache.put(2, 'B')
cache.put(3, 'C')
print("Cache após 3 inserts:", cache.cache)

print("Get(2):", cache.get(2))  # Deve retornar 'B'
cache.put(4, 'D')  # Remove o 1 (menos recente)
print("Cache após put(4, 'D'):", cache.cache)
print("Get(1):", cache.get(1))  # Deve retornar -1 (foi removido)

print("\n==================== Média Salarial ====================\n")

# Pandas – Média Salarial
def media_salarial(df):
    filtrado = df[df['idade'] > 30]
    return filtrado['salario'].mean()

dados = {
    'id': [1, 2, 3, 4, 5],
    'nome': ['Alice', 'Bob', 'Carlos', 'Daniel', 'Eva'],
    'idade': [25, 30, 35, 40, 45],
    'salario': [5000, 7000, 8000, 10000, 12000]
}

df = pd.DataFrame(dados)
media = media_salarial(df)
print("Média salarial (idade > 30):", media)

print("\n==================== Requisições HTTP ====================\n")

# Requisições HTTP Assíncronas
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_urls(urls: list):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)

urls = [
    "https://httpbin.org/get",
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/users/1"
]

def rodar_requisicoes():
    resultados = asyncio.run(fetch_urls(urls))
    for i, conteudo in enumerate(resultados):
        print(f"Resposta {i+1}:\n{conteudo[:200]}...\n{'-'*40}")

rodar_requisicoes()
