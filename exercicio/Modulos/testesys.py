import sys
print(f"plataforma:"{sys.platform}")
print(f"versão do python: %s"{sys.version})
print(f"{len(sys.argv)} argumentos foram passados")
for i in sys.argv:
    print(" - ", i)