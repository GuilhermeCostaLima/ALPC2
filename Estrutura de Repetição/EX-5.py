'''5.Faça um programa para calcular e imprimir a soma dos cubos dos números pares compreendidos entre A e B (B > A). A e B são lidos pelo teclado.'''

a = int(input("valor de A: "))
b = int(input("valor de B: "))

soma = 0

for i in range(a,b + 1):
    if i % 2 == 0:
        cubo = i ** 3
        soma += cubo
print(f'A soma dos cubos dos numeros pares entre {a} e {b} é: {soma}')