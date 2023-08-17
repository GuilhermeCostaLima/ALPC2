'''10. Faça um programa para uma empresa que decide dar um reajuste funcionários de acordo com os seguintes critérios:

50% para aqueles que ganham menos do que três salários mínimos;
20% para aqueles que ganham entre três até dez salários mínimos;
15% para aqueles que ganham acima de dez até vinte salários mínimos;
10% para os demais funcionários.
'''
guardar_sal_50=[]
guardar_sal_20=[]
guardar_sal_15=[]
guardar_sal_10=[]

funcionario = -1
while True:
    reajuste = input("deseja reajustar algum funcionario? digite s ou n: ")
    funcionario += 1
    if reajuste == "s" or reajuste.upper() == "S":
        print(f'funcionario {funcionario}')
        salario = float(input("Digite o salario: "))
        if salario < 4000:
            novo_sal = (salario * 50) / 100
            guardar_sal_50.append(novo_sal)
        elif salario > 4000 and salario <= 13200:
            novo_sal = (salario * 20) / 100
            guardar_sal_20.append(novo_sal)
        elif salario > 13200 and salario <= 26400:
            novo_sal = (salario * 15) / 100
            guardar_sal_15.append(novo_sal)
        else:
            novo_sal = (salario * 10) / 100
            guardar_sal_10.append(novo_sal)
    else:
        break
print("------------------------")
print(f'{len(guardar_sal_50)} tiveram aumento de 50%')
print(f'{len(guardar_sal_20)} tiveram aumento de 20%')
print(f'{len(guardar_sal_15)} tiveram aumento de 15%')
print(f'{len(guardar_sal_10)} tiveram aumento de 10%')
print("------------------------")
func = input("deseja ver o reajuste de um determinado funcinario? digite s ou n ")
if func == "s" or func.upper() == "S":
    print("-------------------------------------------------------")
    print("|ATENÇÃO! A contagem de funcinario sempre começa com 0|")
    print("-------------------------------------------------------")
    criterio = input("Qual reajuste? 50%, 20%, 15%, 10%: ")
    if criterio == "50%" or criterio == "50":
        num_func = int(input("Qual o funcionario? "))
        print(guardar_sal_50[num_func])
    elif criterio == "20%" or criterio =="20":
        num_func = int(input("Qual o funcionario? "))
        print(guardar_sal_20[num_func])
    elif criterio == "15%" or criterio =="15":
        num_func = int(input("Qual o funcionario? "))
        print(guardar_sal_15[num_func])
    elif criterio == "10%" or criterio =="10":
        num_func = int(input("Qual o funcionario?"))
        print(guardar_sal_10[num_func])
else:
    print()
