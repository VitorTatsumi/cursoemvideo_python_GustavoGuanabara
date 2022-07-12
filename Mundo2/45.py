'''
Crie um programa que faça o computador jogar Jokenpô com você
'''

from time import sleep
from random import choice

jokenpo = ['pedra', 'papel', 'tesoura']
opcusu = str(input("Pedra, papel ou tesoura?\n")).lower().strip()
opcpc = choice(jokenpo)

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!')
sleep(0.2)

if opcusu == opcpc:
  print('Empate!\nAmbos escolheram a mesma opção')
elif opcusu == 'pedra' and opcpc == 'papel':
  print('Você perdeu!\nOpção escolhida por você: {}\nOpção escolhida pela máquina: {}'.format(opcusu.title(), opcpc.title()))
elif opcusu == 'pedra' and opcpc == 'tesoura':
  print('Você ganhou!\nOpção escolhida por você: {}\nOpção escolhida pela máquina: {}'.format(opcusu.title(), opcpc.title()))
elif opcusu == 'papel' and opcpc == 'tesora':
  print('Você perdeu!\nOpção escolhida por você: {}\nOpção escolhida pela máquina: {}'.format(opcusu.title(), opcpc.title()))
elif opcusu == 'papel' and opcpc == 'pedra':
  print('Você ganhou!\nOpção escolhida por você: {}\nOpção escolhida pela máquina: {}'.format(opcusu.title(), opcpc.title()))
elif opcusu == 'tesoura' and opcpc == 'papel':
  print('Você ganhou!\nOpção escolhida por você: {}\nOpção escolhida pela máquina: {}'.format(opcusu.title(), opcpc.title()))
elif opcusu == 'tesoura' and opcpc == 'pedra':
  print('Você perdeu!\nOpção escolhida por você: {}\nOpção escolhida pela máquina: {}'.format(opcusu.title(), opcpc.title()))
