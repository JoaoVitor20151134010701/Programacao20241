def montanteFinal(c,i,t):
    m=c*(1+i/100)**t
    return m 


print('''################ JV INVESTIMENTOS CIA ################
      ''')

capital = float(input(f"Digite o seu capital: \n"))
iTaxa = float(input(f"Digite o seu taxa: \n"))
tempo= float(input(f"Digite a o tempo: \n"))
resultadoFinal = montanteFinal(capital,iTaxa,tempo)

print(f"O seu investimento feito em {tempo} meses, deu um resultado final de: R${resultadoFinal:.3f}")
