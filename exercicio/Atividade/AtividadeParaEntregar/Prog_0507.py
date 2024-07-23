z = []
a = []

while True:
    x = input("Insira o nome, quando quiser terminar digite fim: ")
    if x.lower()=="fim":
        break
    else:
        z.append(x)

for i in z:
    if len(i) > 6:
        a.append(i)

for nome in a:
    print(nome)

print("o programa acabô!")                    