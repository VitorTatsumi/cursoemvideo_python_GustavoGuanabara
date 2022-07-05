'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, e acordo com a tabela abaixo:
- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- acima de 40: obesidade mórbida
'''

peso = float(input('Insira o peso: '))
altura = float(input('Insira a altura: '))
imc = peso/(altura*altura)

if imc < 18.5:
  print('IMC: {:.2f}\nAbaixo do peso.'.format(imc))
elif imc < 25:
  print('IMC: {:.2f}\nPeso ideal.'.format(imc))
elif imc < 30:
  print('IMC: {:.2f}\nSobrepeso.'.forma(imc))
elif imc < 40:
  print('IMC: {:.2f}\nObesidade.'.format(imc))
else: 
  print('IMC: {:.2f}\nObesidade mórbida.'.format(imc))
