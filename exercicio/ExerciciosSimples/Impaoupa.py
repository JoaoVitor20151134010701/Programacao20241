n1 = (input("Digite um valor: "))
if not n1.isdecimal():
    print("SÓ NÚMEROS !")
    exit()
n1 = int(n1) 
if  n1%2 ==0:
    print(" O valor ",n1," é par")
else:
    print("O valor de ",n1," é Impar")
