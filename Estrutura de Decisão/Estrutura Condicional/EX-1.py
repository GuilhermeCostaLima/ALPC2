'''1. Faça um programa que leia a primeira letra do estado civil de uma pessoa e mostre uma mensagem com a sua descrição (Solteiro, Casado, Viúvo, Divorciado, Desquitado). Mostre uma mensagem de erro caso for informado um código inválido.'''


nome = input("Seu nome: ")
estado_civil = input("Seu estado civil: ").lower()

if estado_civil.startswith('so'):
    if estado_civil == "solteiro":
        print(f'{nome.capitalize()} está {estado_civil.capitalize()}.')
else:
    if estado_civil.startswith('ca'):
        if estado_civil == "casado":
            print(f'{nome.capitalize()} está {estado_civil.capitalize()}.')
    elif estado_civil.startswith('vi'):
        if estado_civil == "viuvo" or estado_civil == "viúvo":
            print(f'{nome.capitalize()} está {estado_civil.capitalize()}.')
    elif estado_civil.startswith('di'):
        if estado_civil == "divorciado":
            print(f'{nome.capitalize()} está {estado_civil.capitalize()}.')
    elif estado_civil.startswith('de'):
        if estado_civil == "desquitado":
            print(f'{nome.capitalize()} está {estado_civil.capitalize()}.')
    else:
        print("Comando Inválido")