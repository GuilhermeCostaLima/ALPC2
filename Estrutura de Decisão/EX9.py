'''9. Faça um programa que efetue a leitura de três valores numéricos representando os lados de um triângulo. O programa deverá verificar e informar se os lados fornecidos formam realmente um triângulo (cada lado é menor que a soma dos outros dois lados). Se esta condição for verdadeira, deverá ser indicado qual tipo de triângulo foi formado: isósceles (dois lados iguais e um diferente), escaleno (todos os lados diferentes) ou equilátero (todos os lados são iguais).'''


lado1 = float(input("Digite o valor do 1° lado: "))
lado2 = float(input("Digite o valor do 2° lado: "))
lado3 = float(input("Digite o valor do 3° lado: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 and lado1 == lado3:
        print(f'É um triangulo equilatero')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print(f'É um trinagulo isósceles')
    else:
        print(f'É um trinagulo escaleno')
else:
    print(f'Não é um triangulo.')




