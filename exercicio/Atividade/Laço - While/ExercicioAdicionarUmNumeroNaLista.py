v = [ ]

for _ in range(0,10):
    x = int(input("Escreva um numero: "))
    if x in v:
        print("Não posso adicionar")
    else:
        v.append(x)
print(v)