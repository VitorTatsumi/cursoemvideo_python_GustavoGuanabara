#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal, 3 para hexadecimal

num = int(input('Insira um número inteiro:\n'))
opc = int(input('Insira a base de conversão:\n[1] Binário\n[2] Octal\n[3] Hexadecimal\n'))

if opc == 1:
  print('O número [{}] em binário é: {}\n'.format(num, bin(num)[:2]))
elif opc == 2: 
  print('O número [{}] em octal é: {}\n'.format(num, oct(num)[2:]))
elif opc == 3:
  print('O número [{}] em hexadecimal é: {}\n'.format(num, hex(num)[2:]))
else:
  print('Insira uma opção correta!')
