#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

var1 = input('Insira algo:\n')
print('O valor inserido é Alfanumérico? ', var1.isalnum())
print('O valor inserido é somente numérico? ', var1.isnumeric())
print('O valor inserido é somente alfabético? ', var1.isalpha())
print('O valor inserido está somente com maiúsculas? ', var1.isupper())
print('O valor inserido está somente com minúsculas? ', var1.islower())
