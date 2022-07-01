# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

lista = []
for c in range (1,5):
  lista.append(str(input('Insira o {}º nome:\n'.format(c))))

shuffle(lista)

print('\nA ordem de apresentação sorteada foi:')

for c in range(0,4):
  print('{}º: {}'.format(c+1, lista[c]))
