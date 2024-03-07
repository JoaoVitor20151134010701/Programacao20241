'''
Faça um programa que solicite a digitação do nome completo e data
de nascimento de uma só vez, ou seja, um único input deve ser
usado no programa.O programa deverá imprimir o padrão:
Nome<primeiro nome><ultimo nome>
Data de nascimento<data de nascimento>
'''
x =  input("Digite seu Nome e Data de Nascimento: ")
z = x.split()

print(z[0], z[-2])
print(z[-1])





