'''7. Escreva um programa que, a partir de um nome informado pelo usuário, exiba suas iniciais. As iniciais são formadas pela primeira letra de cada nome, sendo que todas deverão aparecer em maiúsculas na saída do programa. Note que os conectores e, do, da, dos, das, de, di, du não são considerados nomes e, portanto, não devem ser considerados para a obtenção das iniciais. As iniciais devem ser impressas em maiúsculas, ainda que o nome seja entrado todo em minúsculas.

Exemplos:

Maria das Graças Pimenta -> MGP
João Carlos dos Santos -> JCS
'''

nome = input("Digite seu nome completo: ").title()

# Separa o nome em uma lista de palavras
palavras = nome.split()

# Cria uma lista para armazenar as iniciais
iniciais = []

# Percorre a lista de palavras
for palavra in palavras:
    # Se a palavra não for um conector, adiciona sua primeira letra à lista de iniciais
    if palavra not in ["e", "do", "da", "dos", "das", "de", "di", "du"]:
        iniciais.append(palavra[0])

# Imprime as iniciais
print("".join(iniciais))