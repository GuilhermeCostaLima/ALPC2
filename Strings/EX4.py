'''4. Leia um código de cinco algarismos (variável Codigo) e gere o digito verificador (DigitoV) módulo 7 para o mesmo. Supondo que os cinco algarismos do código são ABCDE, uma forma de calcular o dígito desejado, com módulo 7 é:

DigitoV = resto da divisão de S por 7, onde S = 6A + 5B + 4C + 3D + 2E'''

codigo = input("Entre o codigo")
if len(codigo) == 5 and codigo.isdigit():
    a = codigo[0]
    b = codigo[1]
    c = codigo[2]
    d = codigo[3]
    e = codigo[4]
    s = 6 * a + 5 * b + 4 * c + 3 * d + 2 * e

    dv = s % 7 
    print(f'digito verificador: {codigo}-{dv}')
else:
    print("Codigo invalido")



