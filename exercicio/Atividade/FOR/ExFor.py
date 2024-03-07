for x in ['spam','eggs','bacon']:
    print(x,end=' ')
print('\nResultado')  

texto= "python"
for i in range(len(texto)):
    print(texto[i], end=' ')
    print("")
    print(i,texto[i])
    print(i,texto[i], end=" ", sep=":")
    print("\n")
    print("")
    print(f"{i}:{texto[i]}")
print("")
print("")
print("")

for i,v in enumerate(texto):
    print(f"{i}:{v}")

