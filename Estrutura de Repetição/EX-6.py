'''6.Faça um programa que receba um valor que foi depositado na poupança e exiba o valor com rendimento mês a mês durante o período de um ano. Considere fixo o juros da poupança em 0,5% a. m.'''

valor = float(input("Valor do deposito: "))
juros = 0.5 / 100

for i in range(1,13):
    rendimento = valor * juros
    valor += rendimento
    print(f'Mês {i} teve um rendimento de R${valor:.2f}')