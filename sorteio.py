from random import choice
A1 = input('Informe o nome do primeiro aluno: ')
A2 = input('Informe o nome do segundo aluno: ')
A3 = input('Infome o nome do terceiro aluno: ')
A4 = input('Informe o nome do quarto aluno: ')
Lista = [A1, A2, A3, A4]
S = choice(Lista)
print('O Aluno sorteado foi {}.'.format(S))
