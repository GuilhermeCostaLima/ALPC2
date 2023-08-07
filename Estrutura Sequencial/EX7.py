'''7. Faça um programa que leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. A fórmula de conversão é: 
℉ = (9 × ℃ + 160) ÷ 5, na qual ℉ é a temperatura em Fahrenheit e ℃ é a temperatura em Celsius.'''


tempc = int(input("Qual a temperatura em °C? "))

fahreinheit = (9 * tempc + 160) / 5

print(f'A temperatura ficará {fahreinheit}°F')