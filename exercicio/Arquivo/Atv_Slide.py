
ListaDados = []

while True:
    nome = input("Digite seu nome( ao terminar digite 'END'): ")
    if nome.lower() == 'end':
        break
    email = input("Digite Seu email: ")
    lista = [nome, email]
    ListaDados.append(lista)

#print(ListaDados)

arq = open('ListadePessoasComEmail.txt','w')
for p in ListaDados:
    dado = ",".join(p)
    arq.write(f"{dado}\n")

arq.close()

print("Arquivo Gerado! ")