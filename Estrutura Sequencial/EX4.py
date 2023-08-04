'''4. Faça um programa para calcular a área de uma circunferência, considerando a fórmula 
AREA = π × RAIO2. Utilize as variáveis AREA e RAIO, a constante π (pi = 3,14159) e os operadores aritméticos 
de multiplicação.'''

print("Calcular a área de uma circunferência")
print("_____________________________________")

# area = float(input("Digite a area: "))
raio = float(input("Digite o raio: "))

raio2 = raio * raio

pi = 3.14159

final = pi * raio2
print(f'A área da circunferência é {final:.2f}')




