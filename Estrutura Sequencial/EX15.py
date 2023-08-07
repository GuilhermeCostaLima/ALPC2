'''15. Considere a seguinte situação: Descontam-se inicialmente 10% do salário bruto do trabalhador como contribuição à previdência social. 
Após esse desconto, há um outro desconto de 5% sobre o valor restante do salário bruto, a título de imposto de renda. Faça um programa que 
leia o salário bruto de um cidadão e imprima o seu salário líquido.'''
import time

salario_bruto = float(input("Qual seu salário bruto? "))

print("Descontando inicialmente 10% do seu salário para a previdência social")
for i in range(3):
    print("...")
    time.sleep(1)

desconto1 = (salario_bruto * 10) / 100
novo_salario = salario_bruto - desconto1
print(f'Seu salario ficou: R${novo_salario:.2f}')

print(f'Aplicando segundo desconto de 5% do restante do seu salário')
for i in range(5):
    print("...")
    time.sleep(1)

desconto2 = (novo_salario * 5) / 100
salario_final = novo_salario - desconto2

print(f'Seu salário líquido é de: R${salario_final:.2f}')