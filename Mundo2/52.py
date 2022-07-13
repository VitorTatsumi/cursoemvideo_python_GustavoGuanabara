'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
'''

num = int(input('Insira um número inteiro: '))
cont = 0

for c in range (1, num+1):
  if num % c == 0:
    cont = cont + 1
if cont == 2:
  print('É um número primo.')
elif cont > 2 or cont < 2:
  print('Não é um número primo.')
