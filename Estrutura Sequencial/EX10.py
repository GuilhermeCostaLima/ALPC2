'''10. Faça um programa que leia os valores de COMPRIMENTO, LARGURA e ALTURA e apresente o valor do volume de uma caixa retangular. 
Utilize para o cálculo a fórmula VOLUME = COMPRIMENTO × LARGURA × ALTURA.'''


comprimento = float(input("Comprimento: "))
largura = float(input("Largura: "))
altura = float(input("Altura: "))

volume = comprimento * largura * altura

print(f'O volume do retangulo é de {volume} ')
