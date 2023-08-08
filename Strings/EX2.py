'''Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.'''

espacos = 0
vogais = 0

frase = input("Informe uma frase: ")
frase = frase.lower()

for i in frase:
    if i == " ":
        espacos += 1
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vogais += 1

print(f'O número de espaços é: {espacos}')    
print(f'O número de vogais é: {vogais}')    


