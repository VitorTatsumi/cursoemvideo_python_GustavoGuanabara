# Faça um programa que leia uma frase qualquer e mostre: quantas vezes aparece a letra "a", em que posição ela aparece a primeira vez, em que posição ela aparece a última vez

frase = str(input("Insira uma frase: \n")).strip().upper()

print('\nQuantidades de letras A: {}\nPosição que ela aparece primeiro: {}\nPosição que ela aparece por último: {}'.format(frase.count('A'), frase.find('A') + 1, frase.rfind('A') + 1))
