'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
'''

frase=str(input('Insira uma frase:\n')).strip().upper()

array = frase.split()
juncao = ''.join(array)

if juncao == juncao [::-1]:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')
