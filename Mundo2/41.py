"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
"""

from datetime import date

anoNasc = int(input('Insira a data de nascimento do atleta: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc

if idade < 10:
  print('Atleta categoria: MIRIM')
elif idade < 15:
  print('Atleta categoria: INFANTIL')
elif idade < 20:
  print('Atleta categoria: JÚNIOR')
elif idade < 26:
  print('Atleta categoria: SÊNIOR')
else:
  print('Atleta categoria: MASTER')
