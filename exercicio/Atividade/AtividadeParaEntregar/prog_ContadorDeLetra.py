'''Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra 'A'
- Em que posição ela aparece a primeira vez
- Em que posição ela aparece a última vez
'''


word = input(f"Digite a frase desejada: \n").lower()
b = list(word)

print(f'A letra aparece {word.count("a")} vezes')
primeiroA= word.find('a')
print(f"A primeira posição o que o a aparece é: {primeiroA}")

ultimoA = word.rfind('a')
print(f"A ultimaposição que o a aparece é: {ultimoA}")



