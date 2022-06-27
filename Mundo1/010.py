#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

#Cotação do dólar em 27/04/2022
dolar = 5.23

howmuchmoney = float(input('Qual o valor deseja converter para dólares?\n'))
print('[R$ {:.2f}]\n[{:.2f} U$D]'.format(howmuchmoney, howmuchmoney/dolar))
