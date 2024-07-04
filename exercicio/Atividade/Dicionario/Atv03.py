#Faça um programa que calcula os juros compostos aplicados a um investimento. Faça uma função que recebe os parâmetros necessários e retorna o montante final 
#aplicando a fórmula de juros compostos. A função recebe um montante inicial, os juros mensais e quantidade de meses e retorna o valor do montante final. 
#No script, faça o código que pede os dados ao usuário e executa a função para calcula o montante final e imprime o resultado na tela.
#Acrescente a funcionalidade de gerar uma lista de dicionários do tipo {"mes": X, "valor": Y}. 
#APós a construção da lista, imprimir a listagem do mês com o valor acumulado daquele mês.

def jurosc (c,i,t):
    montante = c*(1+i/100)**t
    return montante

def listaMeses_(c, i, t):
    lista_meses = []
    for mes in range(1, int(t) + 1):
        montante_mes = jurosc(c, i, mes)
        lista_meses.append({"mes": mes, "valor": montante_mes})
    return lista_meses


Capital = float(input("Digite o capital a ser investido: "))
taxajuros = float(input("Digite a taxa de Juros Mensal: "))
tempo = float(input("Digite o tempo em meses que o dinheiro será investido: "))

montantefinal = jurosc(Capital, taxajuros, tempo)
lista_meses = listaMeses_(Capital, taxajuros, tempo)


print(f'Durante {tempo} meses o seu valor do montante final será de: {montantefinal: .2f}')

print("Listagem do valor acumulado mês a mês:")
for mes_info in lista_meses:
    print(f"Mês {mes_info['mes']}: {mes_info['valor']:.2f}")