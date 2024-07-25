arq = open('ListadePessoasComEmail.txt')
for nome in arq:
    variavel_dosnomes = nome.split(',')
    print(variavel_dosnomes)