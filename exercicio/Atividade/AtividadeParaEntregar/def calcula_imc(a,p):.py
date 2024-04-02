def calcula_imc(a,p):
    return p/(a**2)

def ord_por_imc(dicio):
    return dicio["imc"]


ListaGeral = []
print("###   Para sair Digite 'FIM' na parte Nome.   ###")

while True:
    nome = input("Digite o Nome desejado: ")
    if nome.upper() == "FIM":
        break
    altura = float(input("Digite a sua altura em Metros: "))
    peso = float(input("Digite o seu peso: "))

    imc = calcula_imc(altura, peso)
    v = {"nome": nome, "altura" : altura, "peso" : peso,"imc":imc}
    ListaGeral.append(v)

print(f"Foram cadastradas {len(ListaGeral)} pessoas")

Pessoas_Altura = [p for p in ListaGeral if p["altura"]>1.70]

print(f"Foram cadastradas {len(Pessoas_Altura)} com mais de 1,70m")

pessoas_por_imc = sorted(ListaGeral, key=ord_por_imc)
for p in pessoas_por_imc:
    print(f"{p['nome']}: IMC = {p['imc']}")