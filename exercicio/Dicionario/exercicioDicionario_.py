from random import choice

dicionario = []
while True:
    nome = input('Digite seu nome(para sair digite "n"): ')
    if nome.lower() =="n":
        break
    idade = int(input("Digite sua idade: "))
    tudo = {'nome':nome,'idade':idade}
    dicionario.append(tudo)
totalPessoas = len(dicionario)

print(totalPessoas)
print(f"Pessoas cadastradas: {totalPessoas}")
lista_idades = [i["idade"] for i in dicionario]
print(f'a media de idade e: {sum(lista_idades)/len(lista_idades):.2f}')

p_a = choice(dicionario)
print(f'pessoa aleatoria escolhida: {p_a["nome"]}')
print(dicionario)



