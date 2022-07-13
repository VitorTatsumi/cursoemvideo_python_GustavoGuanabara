'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
'''

from datetime import date
anoatual = date.today().year
menores = 0
maiores = 0

for c in range (0, 7):
  anoNasc = int(input('Insira o ano de nascimento da {}º pessoa: '.format(c+1)))
  if anoatual - anoNasc < 18:
    menores = menores + 1
  elif anoatual - anoNasc >= 18:
    maiores = maiores + 1
print('Há {} maiores de idade e {} menores de idade.'.format(maiores, menores))
