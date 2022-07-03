#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

nomecompleto = str(input('Insira seu nome completo:\n')).strip().upper()
if "SILVA" in nomecompleto:
  print("Este nome contém SILVA")
else: 
  print("Este nome não contém SILVA")
