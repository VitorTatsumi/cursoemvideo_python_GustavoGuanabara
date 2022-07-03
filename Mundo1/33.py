#Faça um programa que leia três números e mostre qual é o maior e qual é o menor

n1 = int(input('Insira o 1º número: \n'))
n2 = int(input('Insira o 2º número: \n'))
n3 = int(input('Insira o 3º número: \n'))

if n1 > n2 and n1 > n3:
  print('O número {} é o maior número inserido.'.format(n1))
elif n2 > n1 and n2 > n3:
  print('O número {} é o maior número inserido'.format(n2))
elif n3 > n1 and n3 > n2:
  print('O número {} é o maior número inserido'.format(n3))

if n1 < n2 and n1 < n3:
  print('O número {} é o menor número inserido'.format(n1))
elif n2 < n1 and n2 < n3:
  print('O número {} é o menor número inserido'.format(n2))
elif n3 < n2 and n3 < n1:
  print('O número {} é o menor número inserido'.format(n3))
