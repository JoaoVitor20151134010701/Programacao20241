x = input(f"Digite sua data de nascimento no formato ddd/mmm/aa:\n")
z = x.split('/')
#print(z)

if z[1] == ('01'):
    z[1] = ' de Janeiro de'
elif z[1] == ('02'):
    z[1] == " Fevereiro de "
elif z[1] == ('de 03'):
    z[1] = ' de Março de '
elif z[1] == ('04'):
    z[1] = ' de abril de'
elif z[1] == ('05'):
    z[1] = ' de Maio de'
elif z[1] ==('06'):
    z[1] = ' de junho de '
elif z[1] == ('07'):
    z[1] = ' de julho de '
elif z[1] == ('08'):
    z[1] = ' de Agosto de '
elif z[1] == ('09'):
    z[1] =' de Setembro de '
elif z[1] == ('10'):
    z[1] = ' de Outubro de '
elif z[1] == ('11'):
    z[1] = ' de Novembro de '
elif z[1] ==('12'):
    z[1] = ' de Dezembro de '
print(f"{z[0]}{z[1]}{z[2]}")


