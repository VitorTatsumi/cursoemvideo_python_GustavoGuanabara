'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto
'''
sexo = str(input('Insira o seu sexo:\n[M] Masculino\n[F] Feminino\n')).lower().strip()

while sexo != 'm' and sexo != 'f':
  sexo = str(input('Opção errada! Insira novamente o seu sexo:\n[M] Masculino\n[F] Feminino\n')).strip().lower()
if sexo == 'm':
  print('Sexo masculino selecionado.')
else:
  print('Sexo feminino selecionado.')
