#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Insira o salário do funcionário: R$'))
print('O salário do funcionário com 15% de aumento é de: R${:.2f}'.format(salario + (salario/100)*15))
