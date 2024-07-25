 
import sys

if len(sys.argv) !=3:
    print("Erro: Digite 'Python3 calcula_rede.py <IP> <MASCARA>'")
    exit(0)

ip = sys.argv[1]
Mask_Ip = sys.argv[2]

Lista_dos_ip = [int(i) for i in ip.split('.')]
l_mascara = [int(m) for m in Mask_Ip.split('.')]

rede_listas = []

for i,m in zip(Lista_dos_ip, l_mascara):
    rede_listas.append(str(i&m))

print(f"Endereço de rede calculado: {'.'.join(rede_listas)}")