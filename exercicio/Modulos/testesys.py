from re import I
import sys
print(f"plataforma: {sys.plataform}")
print(f"Versão do Python: {sys.version}")
print(f"{len(sys.argv)} argumentos foram passados")
for i in  sys.argv:
    print(" - ", i)