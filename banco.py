from tinydb import TinyDB, Query

db = TinyDB('db.json')

def inserir_dados(data, consumo, injecao):
    resultado = injecao-consumo
    db.insert({'data': data, 'consumo': consumo, 'injecao': injecao, 'resultado': resultado})

#inserir_dados('26/10/2025',1179,2186)
print(db.all())