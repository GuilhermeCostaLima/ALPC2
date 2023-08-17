'''6. A empresa paga ao corretor uma comissão calculada de acordo com o valor de suas vendas. Se o valor da venda de um corretor for maior que R$ 50.000,00 a comissão será de 12% do valor vendido. Se o valor da venda do corretor estiver entre R$ 30.000,00 e R$ 50.000,00 (incluindo extremos) a comissão será de 9,5%. Em qualquer outro caso, a comissão será de 7%. Escreva um programa onde será informado nome do corretor e o valor da venda, após isto o programa irá calcular o valor da comissão.'''

nome_corretor = input("Nome do corretor: ")
valor_venda = float(input("Valor da venda: "))

if valor_venda >= 30.000 and valor_venda <= 50.000:
    comissao1 = valor_venda * 0.095
    print(f'O corretor {nome_corretor.capitalize()} terá uma comissao de R${comissao1:.3f}')
elif valor_venda > 50.000:
    comissao2 = valor_venda * 0.12
    print(f'O corretor {nome_corretor.capitalize()} terá uma comissao de R${comissao2:.3f}')
else:
    comissao3 = valor_venda * 0.07
    print(f'O corretor {nome_corretor.capitalize()} terá uma comissao de R${comissao3:.3f}')

