'''10. Anacleto tem 1,50m e cresce 2 centímetros por ano, enquanto Felisberto tem 1,10m e cresce 3 centímetros por ano. 
Construa um programa que calcule e apresente quantos anos serão necessários para que Felisberto seja maior que Anacleto.'''


anacleto = 1.50
felisberto = 1.10
ano = 0

while True:
    ano += 1
    print(f'Ano - {ano}')
    anacleto += 0.02
    felisberto += 0.03
    print(f'Anacleto: {anacleto:.2f}')
    print(f'Felisberto: {felisberto:.2f}')
    print()

    if felisberto > anacleto:
        break 
