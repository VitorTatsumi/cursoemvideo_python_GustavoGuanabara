#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

from math import hypot

catetoOp = float(input('Insira o comprimento do Cateto Oposto: \n'))
catetoAdj = float(input('Insira o comprimento do Cateto Adjacente: \n'))
print('Cateto Adjacente: {}\nCateto Oposto: {}\nHipotenusa: {:.2f}'.format(catetoAdj, catetoOp, hypot(catetoOp, catetoAdj)))
