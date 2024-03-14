L = []
X = ""
while X !="FIM" :
    X = input('Digite um numero: ')
    if X != "FIM":
        L.append(int(X))
print(L)
print([x*3 for x in L])