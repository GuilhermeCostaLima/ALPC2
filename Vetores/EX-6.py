'''6. Escrever um programa que lê um vetor com 20 números inteiros e os imprime na tela. Troque, a seguir, o 1º elemento com o último, o 2º com o penúltimo etc. até o 10º com o 11º e imprima na tela o vetor N assim modificado.
obs:sem criar outro vetor'''

a = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39]
ini = 0
fim = len(a) - 1

print(a)

while ini < fim:
    a[ini],a[fim] = a[fim],a[ini]
    ini += 1
    fim -= 1
print(a)

aux = a[ini]
a[ini]=a[fim]
a[fim]=aux
ini+=1
fim-=1
print(a)