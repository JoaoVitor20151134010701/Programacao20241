import funcao_area as fa 

valor= input("Digite altura e largura: ")
dados = [float(v.strip()) for v in valor.split(',')]

print("Area= ", fa.area(dados[0],dados[1]))

