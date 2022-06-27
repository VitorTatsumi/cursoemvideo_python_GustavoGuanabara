#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

valor = float(input('Insira o valor do produto: \n'))
print('O valor do produto com desconto de 5% é de: R${:.2f}'.format(valor - (valor/100)*5))
