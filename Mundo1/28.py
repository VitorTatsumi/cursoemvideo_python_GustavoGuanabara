#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador

from random import randint

#numPC = randint(0, 5)

num = int(input('Tente descobrir qual o número que o computador pensou!\nInsira um número: \n'))

if randint(0,5) == num:
#if numPC == num:
  print('Você acertou!')
  #print('O número pensado pela máquina foi: {}\n'.format(numPC))
else:
  print('Você errou!')
  #print('O número pensado pela máquina foi: {}\n'.format(numPC))
