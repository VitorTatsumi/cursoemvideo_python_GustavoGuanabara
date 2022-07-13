'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o
'''

lista = []

for c in range (0, 6):
  num = int(input('Insira um número inteiro:'))
  if num % 2 == 0:
    lista.append(num)
  elif num % 2 == 1:
    lista.append(0)
print('A soma de todos os números pares inseridos é: {}'.format(sum(lista)))
