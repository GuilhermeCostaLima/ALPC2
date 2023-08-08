'''imprima todas as posições onde o caracter 'r' usando find'''

f = "O rato roubou a roupa do rei de roma"
c = 0

while True:
    c = f.find("r",c+1)
    if c == -1:
        break
    print(f'{c}')