#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import trunc

numReal = float(input('Insira um número real: \n'))
print('A parte inteira do valor é {}\n'.format(trunc(numReal)))
