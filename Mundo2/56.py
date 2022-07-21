'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos
'''
soma_idade = 0
maior_idade_m = 0
qtd_mulheres = 0

for c in range (0, 4):
  nome = str(input('Insira seu nome: '))
  idade = int(input('Insira a sua idade: '))
  sexo = str(input('Insira seu sexo:\n[M] Masculino\n[F] Feminino\n')).lower().strip()
  #Mesmo sabendo da diversidade de gêneros, optarei por limitar o programa somente à esses dois gêneros para simplificação do mesmo
  soma_idade = soma_idade + idade
  if sexo == 'm':
    if idade > maior_idade_m:
      maior_idade_m = 0
      maior_idade_m = idade
  elif sexo == 'f':
    qtd_mulheres = qtd_mulheres + 1
print('A média de idade do grupo é de {:.0f} anos\nO homem mais velho tem {} anos\nHá {} mulher(es) no grupo\n'.format(soma_idade/4, maior_idade_m, qtd_mulheres))
