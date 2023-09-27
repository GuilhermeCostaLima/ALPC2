'''5. Faça um programa que defina dois vetores A = [2, 4, 7, 13, 14, 15, 16] e B = [1, 6, 7, 11, 13, 16, 18] e faça as seguintes operações de conjuntos:

A ⋃ B: União (todos os valores de ambos os vetores)
A ⋂ B: Intersecção (apenas valores que existam em ambos)
A − B: Diferença (apenas valores que não apareçam simultaneamente em ambos conjuntos)'''



a = [2,4,7,13,14,15,16]
b = [1,6,7,11,13,16,18]
uniao = []
interse = []
diferença = []

for i in a:
    uniao.append(i)
for n in b:
    if n not in a:
        uniao.append(n)
for n in a:
    if n in b:
        interse.append(n)
for n in a:
    if n not in b:
        diferença.append(n)


print(f'união: {uniao}')
print(f'intersecção: {interse}')
print(f'diferença: {diferença}')

