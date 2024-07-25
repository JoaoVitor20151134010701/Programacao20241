'''Faça um script que solicite a entrada do nome e email de pessoas (A
entrada deve terminar ao ser digitado a string "END"). As informações
de cada pessoa (Nome e email) devem ser salva em uma lista. E todas
as listas devem ficar reunidas em uma lista geral. Após isso, o script
deverá salvar essas informações em um arquivo texto aonde cada
pessoa deverá ficar armazenada em uma linha do arquivo e o nome e
email deverão ser separados por vírgula.'''

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