'''Faça um programa que peça ao usuario informar uma frase e imprima a quantidade de letras minúsculas, letras maiúsculas e quantos numeros apareceram'''

frase = input("Informe uma frase: ")
maiusculas = 0
minusculas = 0
numeros = 0
for i in frase: 
    if i.isupper():
        maiusculas += 1
    elif i.islower():
        minusculas += 1
    elif i.isnumeric():
        numeros += 1
        
print("---------")
if numeros == 1:
    print(f'Existe {numeros} numero')
else:
    print(f'Existe {numeros} numeros')
print(f'A quantidade de letras maiusculas é: {maiusculas}')
print(f'A quantidade de letras minusculas é: {minusculas}')