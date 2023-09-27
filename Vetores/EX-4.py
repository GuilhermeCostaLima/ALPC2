'''4.Faça um programa para ler dois vetores V1 e V2 de 15 números cada. Calcular e imprimir a quantidade de vezes que V1 e V2 possuem os mesmos números e nas mesmas posições.'''


v1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
v2 = [1,3,4,6,5,7,8,2,9,12,13,15,10,14,11]

mesmo_numero = 0

for i in v1:
    if(i == v2[mesmo_numero]): #está somando quantos estao na mesma posição e adicionando na variavel mesmo_numero
        mesmo_numero += 1
print(f'{mesmo_numero} estão na mesma posição')
