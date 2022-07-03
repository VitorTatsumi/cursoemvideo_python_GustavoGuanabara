#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

a = int(input('Insira a reta: '))
b = int(input('Insira a reta: '))
c = int(input('Insira a reta: '))

if a + b > c and b + c > a and a + c > b:
  print('Há condições para a existência de um triângulo.')
else:
  print('Não há condições para a existência de um triângulo.')
