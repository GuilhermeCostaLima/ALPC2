'''3. Uma loja fornece 10% de desconto para funcionários e 5% de desconto para clientes vips. Faça um programa que calcule o valor total a ser pago por uma pessoa. O programa deverá ler o valor total da compra efetuada e um código que identifique se o comprador é um cliente comum (1), funcionário (2) ou vip (3).
'''

nome = input("Nome: ")
cliente = int(input("Você é um cliente (1)cliente comum, (2)funcionario ou (3)vip: "))

if cliente == 2:
    valor_compra = float(input("Valor da compra efetuada: "))
    desconto = valor_compra * 0.10
    print(f'Voce funcionario {nome.capitalize()} pagara R${valor_compra - desconto}')
elif cliente == 3:
    valor_compra = float(input("Valor da compra efetuada: "))
    desconto = valor_compra * 0.05
    print(f'Voce cliente Vip {nome.capitalize()} pagara R${valor_compra - desconto}')
else:
    valor_compra = float(input("Valor da compra efetuada: "))
    print(f'Voce cliente comum {nome.capitalize()} pagara R${valor_compra}')


