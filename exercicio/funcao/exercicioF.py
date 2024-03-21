from pprint import pprint
lista = []

print("###########DIGITE QUATRO ANOS PARA SABER SE ELES SÃO BISEXTOS###########")

def eh_bisexto(ano):
    if (ano % 4 == 0 and ano  % 100 != 0) or ano % 400 == 0:
        return True
    return False
    
for _ in range(4):
    valor = int (input("Digite o ano: "))
    bisexto = eh_bisexto(valor)
    lista.append({"ano":valor,'bisexto':bisexto})
pprint(lista)

