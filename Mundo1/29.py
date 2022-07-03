#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite

velocidade = int(input('Insira a velocidade em que o carro está: \n'))

if velocidade > 80:
  print('Você está acima da velocidade!\nVocê foi multado no valor de R${:.2f}'.format((velocidade - 80)*7))
else:
  print('Velocidade permitida.')
