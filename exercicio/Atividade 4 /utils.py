# Arquivo utils.py
def contador_vogais(Texto):
    Q_vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    Texto = Texto.lower()
    for Vogal in Texto:
        if Vogal in Q_vogais:
            Q_vogais[Vogal] += 1
    
    return Q_vogais
