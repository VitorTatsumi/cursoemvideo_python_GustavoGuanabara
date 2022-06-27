#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados

import math 

larg = float(input('Qual a largura da parede?\n'))
alt = float(input('Qual a altura da parede?\n'))
print('A área da parede é de: {:.2f}m\nPara pintar a parede serão necessários: {} baldes de tinta de 1l'.format(larg*alt, math.ceil((larg*alt)/2)))
