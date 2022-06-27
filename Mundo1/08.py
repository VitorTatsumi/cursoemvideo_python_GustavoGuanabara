#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

metros = float(input('Insira um valor em metros: \n'))
print('O valor em milímetros (mm) é: {}\nO valor em centímetros (cm) é: {}\nO valor em decímetros (dm) é: {}\nO valor em quilômetros (km) é: {}\nO valor em hectômetros (hm) é: {}\nO valor em decâmetros (dam) é: {}\n'.format(metros*1000, metros*100, metros*10, metros/1000, metros/100, metros/10))
