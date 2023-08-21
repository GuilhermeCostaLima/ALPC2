'''14.Uma quitanda está vendendo frutas com a seguinte tabela de preços. Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e imprima o valor a ser pago pelo cliente.

            Até 5Kg	        Acima de 5kg
Morango	    R$2,50 / kg	    R$2,20 / kg
Maçã	    R$1,80 / kg	    R$1,50 / kg
'''


tipo = input("Qual fruto voce quer comprar: (MO) para Morango e (MA) para Maçã ").upper()

if tipo == "MO":
    qnt_kilo = int(input("Quantos kg de Morango? "))
    if qnt_kilo <= 5:
        preco = qnt_kilo * 2.50
        print(f'Você pagara R${preco:.2f} em morangos')   
    elif qnt_kilo > 5:
        preco = qnt_kilo * 2.20
        if qnt_kilo == 7:
            print(f'Você pagara R${preco:.2f} em morangos')
    if qnt_kilo > 8 or preco > 25:
        desconto = preco * 0.10
        total_desc = preco - desconto
        print(f'Você pagara R${total_desc:.2f} em morangos')
elif tipo == "MA":
    qnt_kilo = int(input("Quantos kg Maçã? "))
    if qnt_kilo <= 5:
        preco = qnt_kilo * 1.80
        print(f'Você pagara R${preco:.2f} em maçãs')   
    elif qnt_kilo > 5:
        preco = qnt_kilo * 1.50
        if qnt_kilo == 7:
            print(f'Você pagara R${preco:.2f} em maçãs')
    if qnt_kilo > 8 or preco > 25:
        desconto = preco * 0.10
        total_desc = preco - desconto
        print(f'Você pagara R${total_desc:.2f} em maçãs')       
    