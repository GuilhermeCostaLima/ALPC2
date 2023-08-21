'''13.Um posto está vendendo combustíveis com a seguinte tabela de descontos. Escreva um programa que leia o número de litros vendidos e o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 3,30 e o preço do litro do álcool é R$ 2,90.

Álcool	    até 20 litros, desconto de 3% por litro
            acima de 20 litros, desconto de 5% por litro

Gasolina    até 20 litros, desconto de 4% por litro
            acima de 20 litros, desconto de 6% por litro
'''

gasolina = input("Qual tipo de gasolina deseja?(A) para álcool e (G) para gasolina: ")

if gasolina.upper() == "A":
    litros_alc = int(input("Digite a quantidade em litros por favor: "))
    qnt_alc = litros_alc * 2.90
    
    if litros_alc <= 20:
        desconto = litros_alc * 0.03
        valor_total = litros_alc * 2.90 - desconto
        print(f'voce ira pagar R${valor_total}')
    elif litros_alc > 20:
        desconto = litros_alc * 0.05
        valor_total = litros_alc * 2.90 - desconto
        print(f'voce ira pagar R${valor_total}')

elif gasolina.upper() == "G":
    litros_gas = int(input("Digite a quantidade em litros por favor: "))
    qnt_gas = litros_gas * 3.30
    if litros_gas <= 20:
        desconto = litros_gas * 0.04
        valor_total = litros_gas * 3.30 - desconto
        print(f'voce ira pagar R${valor_total}')
    else:
        qnt_gas = litros_gas * 3.30
        desconto = litros_gas * 0.06
        valor_total = litros_gas * 3.30 - desconto
        print(f'voce ira pagar R${valor_total}')