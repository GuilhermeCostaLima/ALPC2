'''8. A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um programa que leia o número de horas trabalhadas em um mês, o salário por hora e imprima o salário total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas).'''

horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salario_por_hora = float(input("Digite o valor do salário por hora: "))

horas_semana = 40
horas_extra = horas_trabalhadas - 40    

salario = horas_semana * salario_por_hora
extra = horas_extra * salario_por_hora * 1.5

salario_total = salario + extra

print(f'Salário total: R${salario_total:.2f}')