#Escolher entre 4 alunos
from random import choice
al1 = input('Nome do primeiro aluno: ')
al2 = input('Nome segundo aluno: ')
al3 = input('Nome terceiro aluno: ')
al4 = input('Nome quarto aluno: ')
print('O aluno escolhido foi {}.'
      .format(choice([al1, al2, al3, al4])))