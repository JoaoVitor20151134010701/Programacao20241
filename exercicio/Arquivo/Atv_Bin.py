import pickle

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
arq.close()

f = open('arquivoBinario.pkl', 'wb')
pickle.dump(ListaDados, f)
f.close()
print("Arquivo Gerado! ")