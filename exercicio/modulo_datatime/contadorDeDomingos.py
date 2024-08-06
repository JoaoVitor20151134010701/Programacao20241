from datetime import datetime, timedelta

mes_ano = input("Digite o mês e ano (MM/YYYY): ")

# Converta a entrada do usuário para um objeto datetime
dia_1 = datetime.strptime(mes_ano, "%m/%Y")

# Calcule o número de dias até o próximo domingo
dif_1 = 6 - dia_1.weekday()

print(f"Domingos do mês {dia_1.strftime('%b')}:")
cont = 0

while True:
    domingo = dia_1 + timedelta(days=dif_1 + cont)
    if domingo.month > dia_1.month:
        break
    print(f"{cont + 1:2d} - {domingo.strftime('%d/%m/%y')}")
    cont += 7
