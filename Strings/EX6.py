'''6.Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak.'''

palavra = input("Digite uma palavra: ")

palavra_leet = {
    "a" :"4",
    "b" :"13",
    "c" :"(",
    "d" :"[)",
    "e" :"3",
    "f" :"|=",
    "g" :"6",
    "h" :"|-|",
    "i" :"|",
    "j" :".]",
    "k" :"|<",
    "l" :"1",
    "m" :"|Y|",
    "n" :"/\/",
    "o" :"0",
    "p" :"|>",
    "q" :"0,",
    "r" :"|2",
    "s" :"5",
    "t" :"7",
    "u" :"[_]",
    "v" :"\/",
    "w" :"\v/",
    "x" :"}{",
    "y" :"`/",
    "z" :"2"
}

leet2 = [palavra_leet[alfabeto] for alfabeto in str(palavra)]
resultado = " ".join(leet2)
print(resultado)