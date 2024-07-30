import json


ListaDados = []

while True:
    nome = input("Digite seu nome( ao terminar digite 'END'): ")
    if nome.lower() == 'end':
        break
    email = input("Digite Seu email: ")
    lista = [nome, email]
    ListaDados.append(lista)

#print(ListaDados)

with open('lista_pessoas.json','w') as f:
    json.dump(ListaDados,f,indent=4)
    