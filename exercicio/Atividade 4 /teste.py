def contador_vogais(Texto):
    # Criado um dicionário para contar as vogais na função.
    Q_vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    Texto = Texto.lower()
    for Vogal in Texto:
        if Vogal in Q_vogais:
            Q_vogais[Vogal] += 1
    
    return Q_vogais

# Solicita ao usuário a frase desejada
Frasedesejada = input("Insira a frase que você deseja contar quantas vogais possui: ")

# Chama a função e exibe o resultado
resultado = contador_vogais(Frasedesejada)
print(resultado)
