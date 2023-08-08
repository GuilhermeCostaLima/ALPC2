'''5. Faça um programa para aprovar empréstimos bancários. O código deve pedir três informações: valor do empréstimo, número de parcelas e salário do solicitante. Aprovar empréstimo caso o valor das parcelas represente no máximo 30% do salário do solicitante.'''

import time

valor_emprestimo = float(input("Digite o valor de emprestimo: "))
numero_parcelas = float(input("Digite o numero de parcelas: "))
salario = float(input("Digite o seu salário: "))

parcela = valor_emprestimo / numero_parcelas

maximo = salario * 0.3
print("----------------------")
for i in range(5):
    print("Calculando...")
    time.sleep(1)
print("----------------------")
if parcela <= maximo:
    print("Emprestimo aprovado")
else:
    print("Emprestimo não aprovado")
