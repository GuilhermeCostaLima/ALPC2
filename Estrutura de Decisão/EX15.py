'''15.Uma Companhia de Seguros possui nove categorias de seguro baseadas na idade e ocupação do segurado. Somente pessoas com pelo menos 17 anos e não mais de 70 anos podem adquirir apólices de seguro. Quanto às classes de ocupações, foram definidos três grupos de risco. A tabela abaixo fornece as categorias em função da faixa etária e do grupo de risco. Dados nome, idade e grupo de risco, determinar a categoria do pretendente à aquisição de tal seguro. Imprimir o nome a idade e a categoria do pretendente, e, caso a idade não esteja na faixa necessária, imprimir uma mensagem.

	        Grupos de risco            
Idades       Baixa Média Alta
17 a 20	      1	    2	  3
21 a 24	      2	    3	  4
25 a 34	      3	    4	  5
35 a 64	      4	    5	  6
65 a 70	      7	    8	  9
'''
nome = input("Qual o seu nome? ")
idade = int(input("Sua idade: "))
grupo_risco = input("Qual seu grupo de risco? Baixo, Médio ou Alto: ").lower()

if idade < 17:
    print("voce nao pode adquirir.")
elif idade > 70:
    print("voce nao pode adquirir.")
else:
    if grupo_risco == "baixo" and 17 <= idade <= 20:
        print(f'{nome.capitalize()} de {idade} anos está na categoria 1')
    elif grupo_risco == "baixo" and 21 <= idade <= 24:
        print(f'{nome.capitalize()} de {idade} anos está na categoria 2')
    elif grupo_risco == "baixo" and 25 <= idade <= 34:
        print(f'{nome.capitalize()} de {idade} anos está na categoria 3')
    elif grupo_risco == "baixo" and 35 <= idade <= 64:
        print(f'{nome.capitalize()} de {idade} anos está na categoria 4')
    elif grupo_risco == "baixo" and 65 <= idade <= 70:
        print(f'{nome.capitalize()} de {idade} anos está na categoria 7')

    if grupo_risco == "medio" and 17 <= idade <= 20:
        print(f'{nome.capitalize()} de {idade} anos está na categoria 2')
    elif grupo_risco == "medio" and 21 <= idade <= 24:
        print(f'{nome.capitalize()} de {idade} anos está na categoria 3')
    elif grupo_risco == "medio" and 25 <= idade <= 34:
        print(f'{nome.capitalize()} de {idade} anos está na categoria 4')
    elif grupo_risco == "medioO" and 35 <= idade <= 64:
        print(f'{nome.capitalize()} de {idade} anos está na categoria 5')
    elif grupo_risco == "medio" and 65 <= idade <= 70:
        print(f'{nome.capitalize()} de {idade} anos está na categoria 8')
    
    if grupo_risco == "alto" and 17 <= idade <= 20:
        print(f'{nome.capitalize()} de {idade} anos está na categoria 3')
    elif grupo_risco == "alto" and 21 <= idade <= 24:
        print(f'{nome.capitalize()} de {idade} anos está na categoria 4')
    elif grupo_risco == "alto" and 25 <= idade <= 34:
        print(f'{nome.capitalize()} de {idade} anos está na categoria 5')
    elif grupo_risco == "alto" and 35 <= idade <= 64:
        print(f'{nome.capitalize()} de {idade} anos está na categoria 6')
    elif grupo_risco == "alto" and 65 <= idade <= 70:
        print(f'{nome.capitalize()} de {idade} anos está na categoria 9')






