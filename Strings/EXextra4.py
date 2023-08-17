'''Faça um programa que peça ao usuario uma palavra ou frase,e informe se o daod informado é um palindromo ou não'''

palavra = input("Digite uma frase ou palavra: ").upper()
inverso = ""
palavra = palavra.replace(" ","")
for i in palavra:
    inverso = i + inverso
    
if palavra == inverso:
        print(f'{palavra} e {inverso} é um palindromo')
else:
    print(f'{palavra} e {inverso} nao é um palindromo')
        
