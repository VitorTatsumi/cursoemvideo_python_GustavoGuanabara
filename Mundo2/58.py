'''
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
'''

import random
num_tentativas = 1
computador = random.randrange(0, 10)
print(computador)
usuario = int(input('Insira um número: '))

while usuario != computador:
  usuario = int(input('Insira novamente um número: '))
  num_tentativas = num_tentativas + 1
print('\nVocê acertou!\nForam necessárias {} tentativas.'.format(num_tentativas))
