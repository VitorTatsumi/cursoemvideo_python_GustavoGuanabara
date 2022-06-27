#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

num = int(input('Insira um número inteiro: \n'))
print('-'*15)
for c in range (1, 11):
  print('{} X {} = {}'. format(num, c, num * c))
print('-'*15)
