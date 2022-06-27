#Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas vindas

nome = str(input('Insira seu nome:\n')).strip(' .!@#$%¨&*()_-.+=/?:;><,\|*')
print('Bem vindo, {}!'.format(nome))
