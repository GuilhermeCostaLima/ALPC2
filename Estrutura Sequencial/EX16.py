'''16. Faça um programa que leia quatro números e apresente os resultados de adição e multiplicação dos valores entre si, 
baseando-se na utilização da propriedade distributiva, ou seja, se forem lidas as variáveis A, B, C e D, devem ser somadas 
e multiplicadas A com B, A com C e A com D; B com C, B com D e por último C com D.'''


a = int(input("A será o número: "))
b = int(input("B será o número: "))
c = int(input("C será o número: "))
d = int(input("D será o número: "))
print("----------------------")
mult1 = a * b
mult2 = a * c
mult3 = a * d
mult4 = b * c
mult5 = b * d
mult6 = c * d

print("Resultado das multiplicações")
print(f'A com B: {mult1}')
print(f'A com C: {mult2}')
print(f'A com D: {mult3}')
print(f'B com C: {mult4}')
print(f'B com D: {mult5}')
print(f'C com D: {mult6}')

