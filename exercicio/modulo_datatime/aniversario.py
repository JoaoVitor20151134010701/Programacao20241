'''Faça um programa que você digita sua data de nascimento (formato
dd/mm/aaaa) e ele vai lhe informar quantos dias faltam para o seu
próximo aniversário'''

from datetime import datetime
import locale
agora = datetime.now()
niver = input("Digite a data do seu aniversário utilizando '/' para separá-los: ")
dataFormatada = datetime.