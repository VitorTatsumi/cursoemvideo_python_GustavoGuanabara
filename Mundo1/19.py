#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.Faça um programa que ajude ele, lendo o nome deles e escrevendo o do escolhido.

from random import choice

lista = []
for c in range (1,4):
  lista.append(str(input('Insira o {}º nome: \n'.format(c))))

print('O aluno sorteado é o: {}\n'.format(choice(lista)))
