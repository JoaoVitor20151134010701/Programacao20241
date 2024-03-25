#-------------------------------------------------------------------------------
# Name:João Vitor Santos
# Matrícula: 20231014050041
#-------------------------------------------------------------------------------
print('''
########## BEM VINDO A CEMMONEY - O banco da galera ! ##########''')
print("")

#Valor para entrada
valor = float(input("Valor de Saque? ->   "))
#Verificação de entrada
if  valor <= 1000:
    if valor <= 0: 
        print("############ Não é possível atender ao pedido! ##########")

    nota_100 = valor//100
    print("Número de notas de 100: ",nota_100)

    valor = valor-nota_100*100
    #valor=%100 - resto da divisão

    nota_50=valor//50
    valor = valor-nota_50*50
    print("Número de notas de 50: ",nota_50)

    nota_20=valor//20
    valor = valor-nota_20*50
    print("Número de notas de 20: ",nota_20)

    nota_10=valor//10
    valor = valor-nota_10*10
    print("Número de notas de 10: ",nota_10)

    nota_5=valor//5
    valor = valor-nota_5*10
    print("Número de notas de 5: ",nota_5)

else:
    print("############ Não é possível atender ao pedido! ##########")
