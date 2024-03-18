dicionario = []
while True:
    nome = input('Digite seu nome(para sair digite "n"): ')
    if nome.lower() =="n":
        break
    idade = int (input("Digite sua idade: "))
    tudo = {'nome':nome,'idade':idade}
    dicionario.append(tudo)
totalPessoas = len(dicionario)
print(totalPessoas)
print(f"Pessoas cadastradas{totalPessoas}")
print(dicionario)



