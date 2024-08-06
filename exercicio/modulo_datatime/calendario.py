import calendar
from datetime import datetime

# Obtenha o mês e ano atual
mes_atual = datetime.now().month
ano_atual = datetime.now().year

# Imprima o calendário do mês atual em português
print(calendar.month(ano_atual, mes_atual, w=0, l=0))
