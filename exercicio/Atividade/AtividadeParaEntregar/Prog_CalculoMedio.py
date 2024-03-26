'''Faça um programa que recebe 4 notas 
de um aluno referente às notas dos quatro 
bimestres e calcula a média parcial baseado 
na fórmula fornecida abaixo. De acordo com as
regras de aprovação também listadas abaixo, 
encontre o status do aluno (Aprovado, Recuperação e Reprova) e, 
caso o aluno esteja em recuperação, calcule a nota da prova de
 recuperação necessária para aprovação.

Status:
Aprovado: Média >= 70
Recuperação: 20 <= Média < 70
Reprovado: Média < 20



'''

n1 = float (input("Digite a sua primeira Nota: "))
n2 = float (input("Digite a sua segunta Nota: "))
n3 = float (input("Digite a sua terceira Nota: "))
n4 = float (input("Digite a sua quarta Nota: "))
 
nMax = 100
nMin = 60 
mediaAluno = (n1+n2+n3+n4)/4

if mediaAluno >= 70:
    print("Parabéns - APROVADO GALADO!")
elif mediaAluno <= 19:
    print("Ihh man - REPROVADO!")  
else:
    print('''Você está em recuperação!

    ''')
    notaFinal = 60
    nota_necessaria = notaFinal * 2 - mediaAluno
    print("Para passar, você precisa obter pelo menos:", nota_necessaria)

