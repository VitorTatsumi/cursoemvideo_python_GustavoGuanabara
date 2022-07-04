"""
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
"""

r1 = float(input('Insira o primeiro comprimento de reta: '))
r2 = float(input('Insira o segundo comprimento de reta: '))
r3 = float(input('Insira o terceiro comprimento de reta: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('As condições para existência de um triângulo estão compatíveis')
    if r1 == r2 == r3:
        print('Este é um Triângulo Equilátero')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('Este é um Triângulo Isósceles')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('Este é um Triângulo Escaleno')
else:
    print('Não há condições para existência de um triângulo.')
