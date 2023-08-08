'''1. Faça um programa que peça dois números e imprima o maior deles.'''

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

if num1 > num2:
    print(f'O maior é o {num1:.0f}')
else:
    print(f'O maior é o {num2:.0f}')