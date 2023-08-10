'''imprima todas as posições onde o caracter 'r' usando find'''

f = "O rato roubou a rica roupa do rei da russia"
c = 0

while True:
    c = f.find("r",c+1)
    if c == -1:
        break
    print(f'O r está na posição {c}')
