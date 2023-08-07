'''12. Faça um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar um determinado cômodo de uma residência. 
Dados de entrada: a potência da lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do cômodo. 
Considere que a potência necessária é de 18 watts por metro quadrado.'''

potencia_lampada = float(input("Potencia da lampada (em watts): "))
print("-------------------------------")

print("Dimensões do cômodo (em metros)")
largura = float(input("Largura : "))
comprimento = float(input("Comprimento: "))
metro_quadrado = largura * comprimento

lamp_por_metro_quadrado = metro_quadrado * 18

qnt_lampadas = lamp_por_metro_quadrado / potencia_lampada

print(f'Será necessário {int(qnt_lampadas)} lampadas')