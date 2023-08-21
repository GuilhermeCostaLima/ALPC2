'''11.Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raízes reais; informe-as ao usuário.'''
import math

a = int(input("Digite o valor de a: "))
if a == 0:
    print("Não é equação de segundo grau.")
else:
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))

    delta = (b**2) - 4 * a * c
    
    if delta == 0:
        raiz1 = ((-b**2) + math.sqrt(delta)) / 2 * a
        raiz2 = ((-b**2) - math.sqrt(delta)) / 2 * a
        print(f'delta={delta} então possui uma raiz real, raiz={raiz1}')
    elif delta < 0:
        print(f'A equação não possui raiz pois delta= {delta} é negativo')
    else:
        raiz1 = ((-b**2) + math.sqrt(delta)) / 2 * a
        raiz2 = ((-b**2) - math.sqrt(delta)) / 2 * a
        print(f'delta={delta} possui duas raizes, {raiz1,raiz2}')

    