#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

nome = str(input('Insira o nome completo: \n')).strip().split()
print('\nO primeiro nome é: {}\nO último nome é: {}\n'.format(nome[0], nome[-1]))
