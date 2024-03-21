'''Faça um programa que recebe a digitação de 4 anos e 
retorna uma lista de dicionário no seguinte formato:
{"ano": 2003, "bisexto": False} para cada ano digitado 
indicando se o ano é bisexto ou não;
'''
from pprint import pprint
lista = []
print("###########DIGITE QUATRO ANOS PARA SABER SE ELES SÃO BISEXTOS###########")


for i in range(4):
    ano = int (input(f'Digite um ano: \n'))
    if (ano % 4 == 0 and ano  % 100 != 0) or ano % 400 == 0:
        verdade = {"ano": ano,"bissexto": True}
        lista.append(verdade)
    else:
        lista.append({"ano": ano, "bissexto":False})
        
pprint(lista)
