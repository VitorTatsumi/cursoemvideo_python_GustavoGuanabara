#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit

gCelsius = int(input('Insira uma temperatura em °C: \n'))
print('{}\n{}ºC\n{}°F\n{}\n'.format('-'*30, gCelsius, (gCelsius * 1.8 + 32), '-'*30))
