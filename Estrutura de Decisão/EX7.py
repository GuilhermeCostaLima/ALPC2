'''7. Faça um programa onde serão informados as quatro notas do aluno. O programa irá então apresentar a média, se foi aprovado (nota ≥ 7) ou se ficou em exame. Caso o aluno ficou em exame, o programa irá então perguntar qual foi a nota do exame e então irá calcular a nova média (média anteior com a nota do exame) e informar se ele foi aprovado (nova média ≥ 5) ou se foi reprovado.'''

contador = 1
nota_total = 0

while contador <= 4:
    nota_aluno = float(input(f'Nota {contador} do aluno: '))
    contador += 1
    nota_total += nota_aluno
media = nota_total/4
if media >= 7:
    print(f'Este aluno foi aprovado com media {media}')
else:
    print(f'Este aluno ficou em exame com media {media}')
    print("--------------------------------------------")
    enter = input("Para calcular se passou no exame pressione enter:")
    nota_exam = float(input("Digite a nota do exame: "))
    nova_media = (media + nota_exam) / 2
    print(f'A nova media {nova_media}')
    print()
    if nova_media >= 5:
        print("Aprovado!")
    else:
        print("Reprovado.")
