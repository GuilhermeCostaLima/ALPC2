'''2. Faça um programa que leia três números e imprima o maior deles.'''

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

if num2 < num1 > num3:
    print(f'o maior é {num1}')
elif num1 < num2 > num3:
    print(f'o maior é {num2}')
else:
    print(f'o maior é {num3}')