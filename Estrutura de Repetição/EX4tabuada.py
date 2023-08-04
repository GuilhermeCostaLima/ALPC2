'''4. Construa um programa que exiba a tabuada de 1 até N, onde N é informado pelo usuário. ex: Até a tabuada de 3, irá imprimir as tabuadas de 1, 2 e 3.'''

tab = int(input(f'Digite ate qual tabuada voce quer: '))

for tabuada in range(1,tab+1):
  print(f'Tabuada do {tabuada}:')
  for num in range(1,11):
    resultado = tabuada * num
    print(f'{tabuada} X {num} = {resultado}')
