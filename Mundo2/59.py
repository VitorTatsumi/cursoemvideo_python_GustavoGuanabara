'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso
'''

valor1 = int(input('Insira o primeiro valor: '))
valor2 = int(input('Insira o segundo valor: '))
opc = int(input('\nInsira a opção desejada:\n[ 1 ] Somar valores\n[ 2 ] Multiplicar valores\n[ 3 ] Maior número\n[ 4 ] Inserir novos números\n[ 5 ] Sair do programa\n'))

while opc != 5:
  if opc == 4:
    valor1 = int(input('Insira o primeiro valor: '))
    valor2 = int(input('Insira o segundo valor: '))
  elif opc == 3:
    if valor1 == valor2:
      print('Não há maior pois os valores são iguais.')
    elif valor1 > valor2:
      print('O maior valor é o {}'.format(valor1))
    elif valor2 > valor1:
      print('O maior valor é o {}'.format(valor2))
  elif opc == 2:
    print('O resultado da multiplicação dos valores é de: {}'.format(valor1*valor2))
  elif opc == 1:
    print('O resultado da soma dos valores é de: {}'.format(valor1 + valor2))
  opc = int(input('\nInsira a opção desejada:\n[ 1 ] Somar valores\n[ 2 ] Multiplicar valores\n[ 3 ] Maior número\n[ 4 ] Inserir novos números\n[ 5 ] Sair do programa\n'))
print('Volte sempre! :)')
