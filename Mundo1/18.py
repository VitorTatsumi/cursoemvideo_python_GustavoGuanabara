#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

angulo = float(input('Insira um ângulo de uma circunferência: \n'))
print('Ângulo: {}\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(angulo, math.sin(angulo), math.cos(angulo), math.tan(angulo)))
