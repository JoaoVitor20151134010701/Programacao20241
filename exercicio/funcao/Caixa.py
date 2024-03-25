def caixa_eletronico(valor_saque):
    # Verifica se o valor está dentro do limite permitido
    if valor_saque <= 0 or valor_saque > 1000:
        return "Não é possível atender ao pedido. O valor deve estar entre R$ 1,00 e R$ 1.000,00."

    # Define os valores das cédulas disponíveis
    cedulas = [100, 50, 20, 10, 5]

    # Inicializa o dicionário para armazenar a quantidade de cada cédula
    quantidade_cedulas = {}

    # Calcula a quantidade de cada cédula
    for cedula in cedulas:
        quantidade = valor_saque // cedula
        valor_saque %= cedula
        if quantidade > 0:
            quantidade_cedulas[cedula] = quantidade

    # Monta a mensagem com as cédulas a serem entregues
    mensagem = "Cédulas a serem entregues:\n"
    for cedula, quantidade in quantidade_cedulas.items():
        mensagem += f"R${cedula:.2f}: {quantidade} cédula(s)\n"

    return mensagem

# Exemplo de uso
valor_saque = float(input("Digite o valor que deseja sacar (R$ 1,00 a R$ 1.000,00): "))
resultado = caixa_eletronico(valor_saque)
print(resultado)
