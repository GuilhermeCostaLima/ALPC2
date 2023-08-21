'''3.Faça um programa que peça dois números, base e expoente, calcule e imprima o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.'''

base = int(input("Digite o numero base: "))
expo = int(input("Digite o expoente: "))
total = base
for i in range(expo - 1):
    total *= base
print(f'O resultado de {base} elevado a {expo} é: {total}')



