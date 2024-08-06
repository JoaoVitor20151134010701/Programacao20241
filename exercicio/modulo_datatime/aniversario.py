'''Faça um programa que você digita sua data de nascimento (formato
dd/mm/aaaa) e ele vai lhe informar quantos dias faltam para o seu
próximo aniversário'''

from datetime import date
niver = input("Digite sua data (dia/mes/ano): ")

niver_lista = [int(d) for d in niver.split("/")]
hoje = date.today()
niver_esseano = date(hoje.year, niver_lista[1],niver_lista[0])

if hoje > niver_esseano:
    niver_proxano = date(hoje.year+1,niver_lista[1],niver_lista[0])
    dif = niver_proxano - hoje
else:
    dif = niver_esseano - hoje

if dif.days != 0 :
    print(f"faltam {dif.days} pro teu aniversario")
else:
    print("parabéns para voce! ")    