#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de R$ 15%.

salario = float(input('Insira o valor do salário do funcionário: \nR$'))

if salario > 1250:
  print('O valor atual do salário com aumento de 10% é de: R${:.2f}'.format((salario + (salario/100)*10)))
else: #salario <= 1.250:
  print('O valor atual do salário com aumento de 15% é de: R${:.2f}'.format((salario + (salario/100)*15)))
