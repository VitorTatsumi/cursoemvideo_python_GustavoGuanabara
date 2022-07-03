#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "Santo"

nomeCid = str(input('Insira o nome de uma cidade: \n')).strip().upper().split()

if nomeCid[0] == 'SANTO':
  print('A cidade possui a palavra SANTO em seu nome.')
else:
  print('A cidade não possui a palavra SANTO em seu nome.')
