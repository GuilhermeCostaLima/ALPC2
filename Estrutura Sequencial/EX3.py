'''3. Faça um programa que leia três notas de um aluno, calcule e escreva a média final deste aluno. 
Considerar que a média é ponderada e que o peso das notas é 2, 3 e 5.'''

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))

# peso1 = n1 * 2
# peso2 = n2 * 3
# peso3 = n3 * 5

mfinal = ((n1 * 2)+(n2 * 3)+(n3 * 5))/10
print(f'Media final: {mfinal}')