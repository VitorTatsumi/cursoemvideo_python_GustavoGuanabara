#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade: Se ele ainda vai se alistar ao serviço militar. Se é a hora de se alistar. Se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo

from datetime import datetime

anonasc = int(input('Insira o seu ano de nascimento: '))
anoatual = datetime.now().year

if anoatual - anonasc < 18:
  print('Você ainda irá se alistar.\nFaltam {} anos.'.format(18 - (anoatual - anonasc)))
elif anoatual - anonasc == 18:
  print('Está na hora de você se alistar.')
elif anoatual - anonasc > 18:
  print('Você já passou do prazo para se alistar.\nPassaram-se {} anos'.format((anoatual - anonasc)-18))
