'''Utilizando apenas lista, faça um programa que solicita a entrada de
quatro nomes de alunos, monte uma lista e escolha aleatoriamente
um desses nomes. A saída será a impressão do nome escolhido'''

from random import choice

lista = []

for i in range(0,4):
    b = input(f'Digite seu nome: \n')
    lista.append(b)
print(f'O nome escolhido aleatoriamente foi: ', choice(lista))


