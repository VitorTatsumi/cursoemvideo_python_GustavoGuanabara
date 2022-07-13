'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão
'''

termo = int(input('Insira o primeiro termo da progressão: '))
razao = int(input('Insira a razão: '))

for c in range (0, 10):
  print(termo, end=' -> ')
  termo = termo + razao
print('FIM')
