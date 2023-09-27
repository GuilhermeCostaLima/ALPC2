'''1. Fazer um algoritmo que calcule e imprima o soma, a média, o maior e o menor dos valores armazenados em um vetor A de 100 elementos numéricos a serem lidos do dispositivo de entrada padrão.'''


import random

v = []
maior = 0
menor = 0
ini = True
soma = 0
for i in range(100):
    v.append(random.randint(0,1000))
    
    for n in v:
        soma += n
        if ini:
            maior = n 
            menor = n
            ini = False
        if n > maior:
            maior = n
        if n < menor:    
            menor = n
            

print(f'O maior numero é: {maior}')
print(f'O menor numero é: {menor}')
print(f'Soma de todos: {sum(v)}')
print(f'media: {sum(v)/100}')