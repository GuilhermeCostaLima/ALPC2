'''11. Faça um programa que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. 
Considerar ano com 365 dias e mês com 30 dias. Calcular quantos dias a pessoa já viveu até hoje.'''

idade = int(input("Sua idade: "))
mes = int(input("Mês atual: "))
dias = int(input("Dia atual: "))

dias_vividos = (idade * 365) + (mes * 30) + dias

print(f'Você viveu {dias_vividos} dias até hoje')
