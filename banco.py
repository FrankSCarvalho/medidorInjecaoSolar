from tinydb import TinyDB, Query

CAMINHO_BANCO = "db.json"

def abrir_banco():
    return TinyDB(CAMINHO_BANCO, indent=4, ensure_ascii=False, encoding='utf-8')

def inserir_dados(data, consumo, injecao):
    db = abrir_banco()
    consumo = int(consumo)
    injecao = int(injecao)
    resultado = injecao-consumo
    
    db.insert({'data': data, 'consumo': consumo, 'injecao': injecao, 'resultado': resultado})

    db.close()

