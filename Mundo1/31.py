#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km e R$ 0,45 para viagens mais longas

km = float(input('Qual a distância da viagem em quilômetros? (Km)\n'))

if km <= 200:
  print('O valor da passagem é de: R${:.2f}'.format(0.50*km))
elif km > 200:
  print('O valor da passagem é de: R${:.2f}'.format(0.45*km))
