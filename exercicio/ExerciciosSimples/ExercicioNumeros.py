largura = int(input("Digite a largura (Em metros): "))
altura = int(input("Digite a altura(Em metros): "))
comprimento = int(input("Digite o comprimento(Em Metros)"))
redimento =  int(input("Qual o rendimento da tinta em m2/l: "))
 
area = 2*(largura+comprimento)*altura
print("Área Total é: ",area)
volumeTinta = 2*area/redimento

print("Litro de tinta gasto = ", volumeTinta)