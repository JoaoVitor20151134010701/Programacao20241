'''Faça um programa que calcule a soma
entre todos os números que são múltiplos 
de três e que se encontram no intervalo 
de 1 até 500'''

x = 0 
for y in range(1,501):
    if y % 3 ==0:
        x=x+y
print(x)



