'''4. As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12 unidades. Escreva um programa que leia o número de maçãs compradas, calcule e imprima o custo total da compra.'''

maca = int(input("Quantas maças irá comprar? "))

if maca < 12:
    preco_qntd = maca * 1.30
    print(f'{maca} maças será R${preco_qntd:.2f}')
else:
    preco_mais = maca * 1
    print(f'{maca} maça será R${preco_mais:.2f}')
