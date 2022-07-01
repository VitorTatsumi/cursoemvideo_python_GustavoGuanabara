#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = str(input('Insira um número de 0 a 9999:\n'))

print('Unidade: {}\nCentena: {}\nDezena: {}\nMilhar: {}\n'.format(num[3], num[2], num[1], num[0]))

