'''Faça um programa que leia o nome,
a altura e o peso de várias pessoas
(Sem quantidade definida), guardando-os 
tudo em uma lista de dicionários (as informações 
de cada pessoa são armazenadas em um dicionário). No final, mostre: 
Uma listagem com os nomes das pessoas ordenada por peso
Quantas pessoas tem mais de 1.70m
Uma listagem com os nomes das pessoas ordenada por IMC'''

listaGeral = []
#Adicionando nome, altura e peso das pessoa em uma lista de dicionario
print('''############### DIGITE - 'FIM' PARA FINALIZAR EM "DIGITE SEU NOME " ###############
''')
while True:
    nome = (input("Digite seu nome (Digite 'fim' para interromper o processo!):"))
    if nome.upper() == 'FIM':
        break
    altura = float(input("Digite seu altura:"))
    peso = int(input("Digite seu peso:"))
    imc = peso / (altura/100) ** 2
    geral= {"nome":nome,"altura":altura,"peso":peso,"imc":imc}
    #a lista ira receber a lista de dicionario 
    listaGeral.append(geral)
    #parar o programa SE o user digiter Fim
    # Ordenar a lista de pessoas por peso
listaGeral = sorted(listaGeral, key=lambda x: x["peso"])

# Listagem dos nomes das pessoas ordenadas por peso
print("Listagem de pessoas ordenadas por peso:")
for pessoa in listaGeral:
    print(pessoa["nome"])

# Contar quantas pessoas têm mais de 1.70m de altura
maiorQue170 = sum(1 for pessoa in listaGeral if pessoa["altura"] > 1.70)
print("Número de pessoas com mais de 1.70m de altura:", maiorQue170)

# Ordenar a lista de pessoas por IMC
listaGeral = sorted(listaGeral, key=lambda x: x["imc"])

# Listagem dos nomes das pessoas ordenadas por IMC
print("\nListagem de pessoas ordenadas por IMC:")
for pessoa in listaGeral:
    print(pessoa["nome"])
