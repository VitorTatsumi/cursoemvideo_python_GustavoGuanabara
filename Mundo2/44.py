'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal, e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- em 3x ou mais no cartão: 20% de juros
'''

valorProd = float(input('Insira o valor do produto:\nR$'))
opc = int(input('Insira a forma de pagamento:\n[1]À vista (Dinheiro ou Cheque)\n[2]À vista no cartão\n[3]2x no cartão\n[4]3x ou mais no cartão\n'))

if opc == 1:
  print('Desconto de 10% no valor do produto!\nValor final: R${}'.format(valorProd - ((valorProd/100)*10)))
elif opc == 2:
  print('Desconto de 5% no valor do produto!\nValor final: R${}'.format(valorProd - ((valorProd/100)*5)))
elif opc == 3:
  print('Sem desconto! Valor do produto: R${}'.format(valorProd))
elif opc == 4:
  print('Juros de 20%!\nValor do produto: R${}'.format(valorProd + ((valorProd/100)*20)))
