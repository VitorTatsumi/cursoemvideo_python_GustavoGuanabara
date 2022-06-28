#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais elefoi alugado. Calcule o preço à pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por KM rodado.

km = float(input('Qual a quantidade de Kms rodados pelo veículo?\n'))
dias = int(input('Qual a quantidade de dias?\n'))
print('Quilômetros rodados: {}km\nDias de locação: {}\nO total à pagar é de: R${:.2f}\n'.format(km, dias, (km*0.15) + dias*60))
