#Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas e minúsculas, quantas letras ao todo (sem considerar espaços), quantas letras tem o primeiro nome.

nomeCompleto = str(input('Insira seu nome completo: \n'))
print('\nO nome completo com:\nLetras maiúsculas: {}\nLetras minúsculas: {}\nQuantidades de letras (sem considerar espaços): {}\n'.format(nomeCompleto.upper().strip(), nomeCompleto.lower().strip(), len(nomeCompleto.replace(' ', ''))))

nomeSeparado = nomeCompleto.split()

print('Quantidades de letras do primeiro nome: {}'.format(len(nomeSeparado[0])))
