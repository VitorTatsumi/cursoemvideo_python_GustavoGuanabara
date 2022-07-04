#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input('Qual o valor do imóvel?\nR$'))
salario = float(input('Qual o salário do comprador?\nR$'))
anos = int(input('Será pago em quantos anos?\n'))
valorPrestacao = valorCasa/(anos*12)

if valorPrestacao > (salario/100)*30:
  print('Empréstimo negado!')
else:
  print('Empréstimo autorizado!\nO valor da prestação é de: R${:.2f}'.format(valorPrestacao))
