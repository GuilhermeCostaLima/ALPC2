'''12.Faça um programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto. Regras para o cálculo dos anos bissextos:

De 4 em 4 anos é ano bissexto.
De 100 em 100 anos não é ano bissexto.
De 400 em 400 anos é ano bissexto.
Prevalecem as últimas regras sobre as primeiras
'''

ano = int(input("Digite um ano: "))

if ano % 4 == 0:
    print(f'{ano} é um ano bissexto.')
elif ano % 100 != 0:
    print(f'{ano} não um ano bissexto.')    
elif ano % 400 == 0:
    print(f'{ano} é um ano bissexto.')

