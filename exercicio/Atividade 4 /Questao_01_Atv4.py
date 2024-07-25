  # Cria um dicionário vazio para armazenar o resultado
def inverte_dicionario(d):
  
    resultado = {}
      
    for c, valor in d.items():
        if valor not in resultado:
            resultado[valor] = []
        resultado[valor].append(c)
    
    return resultado

dicionario_original = { "a": 10, "b": 23, "c": 10, "d": 15 }
dicionario_invertido = inverte_dicionario(dicionario_original)
print(dicionario_invertido)
