'''5.Escreva um programa que dado um valor numérico digitado pelo usuário (armazenado em uma variável inteira), imprima cada um dos seus dígitos por extenso.
Exemplo:
Entre o número: 4571
Resultado: quatro, cinco, sete, um
'''

num = int(input("Digite qualquer numero: "))

numeros = {
    "0": "zero",
    "1": "um",       
    "2": "dois",       
    "3": "três",       
    "4": "quatro",      
    "5": "cinco",       
    "6": "seis",
    "7": "sete",       
    "8": "oito",       
    "9": "nove"
}

numeros2 = [numeros[digito] for digito in str(num)]
resultado = ", ".join(numeros2)
print(resultado)