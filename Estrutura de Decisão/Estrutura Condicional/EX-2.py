'''2. Faça um programa que leia dois valores do usuário e a operação que ele deseja executar (Operações: (+) soma, (-) subtração, (/) divisão, (*) multiplicação). Execute a operação desejada e imprima na tela.'''

numb1 = float(input("Digite o primeiro numero: "))
operacao = input("Qual operacao deseja: (+)soma, (-)subtração, (/)divisão ou (*)multiplicação: ")
numb2 = float(input("Digite o primeiro numero: "))

if operacao == "+":
    resultado = numb1 + numb2
    print(f'Resultado: {resultado}')
elif operacao == "-":
    resultado = numb1 - numb2
    print(f'Resultado: {resultado}')
elif operacao == "*":
    resultado = numb1 * numb2
    print(f'Resultado: {resultado}')
elif operacao == "/":
    resultado = numb1 / numb2
    print(f'Resultado: {resultado}')