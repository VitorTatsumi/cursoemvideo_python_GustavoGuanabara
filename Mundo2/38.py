#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: o primeiro valor é maior, o segundo valor é maior, não existe valor maior; os dois são iguais

n1 = int(input('Insira o primeiro número inteiro: \n'))
n2 = int(input('Insira o segundo número inteiro:\n'))

if n1 > n2:
  print('O primeiro valor é maior.\nValor 1: {}\nValor 2: {}\n'.format(n1, n2))
elif n1 < n2:
  print('O segundo valor é maior.\nValor 1: {}\nValor 2: {}\n'.format(n1, n2))
elif n1 == n2:
  print('Os dois valores são iguais, não existe valor maior.\nValor 1: {}\nValor 2: {}\n'.format(n1, n2))
