'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos
'''

listPeso = []

for c in range (0, 5):
  peso = float(input('Insira o peso da {}º pessoa: '.format(c+1)))
  listPeso.insert(c, peso)
print('O maior peso é: {}Kg\nO menor peso é: {}Kg\n'.format(max(listPeso), min(listPeso)))
