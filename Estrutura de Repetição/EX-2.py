'''2.Escreva um programa que pergunte ao usuário um número e após, imprima na tela a soma total de 1 até o número lido. Exemplo: 5: 1 + 2 + 3 + 4 + 5 = 15'''

num = int(input("Que numero deseja? "))
soma = 0
for i in range(num + 1):
    soma += i
print(soma)