'''3. Faça um programa que receba como entrada três valores e os imprima em ordem crescente.'''

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))
print()
print("Colocando em ordem crescente")
print("-----------------------")
if num1 < num2 < num3:
    print(num1,num2,num3)
elif num1 < num3 < num2:
    print(num1,num3,num2)
elif num2 < num1 < num3:
    print(num2,num1,num3)
elif num2 < num3 < num1:
    print(num2,num3,num1)
elif num3 < num1 < num2:
    print(num3,num1,num2)
else:
    print(num3,num2,num1)    
    



