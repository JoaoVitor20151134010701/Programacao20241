from pprint import pprint

def mes_xtenso(mes):
    meses = ["Janeiro", "fevereiro", "março", "Abril", "Maio", "Junho", "julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    return meses[int(mes) -1 ]

data = input("Digite a data (dd/mm/aa)")
data = data.split("/")

print(f'{data[0]} de {mes_xtenso(data[1])} de data {data[2]}')
