#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input('Insira o primeiro termo da progressão: '))
razao = int(input('Insira a razão: '))
c = 0

while c < 10:
  print(termo, end=' -> ')
  termo = termo + razao
  c = c + 1
print('FIM')
