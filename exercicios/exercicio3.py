# programa que recebe uma idade e diga se é maior ou menor de idade

from math import sqrt

def calcularBaskara(a,b,c):

    beta = b * (-1)
    delta = (b**2) - 4 * (a * c)
    base = 2*a

    # print(beta)
    # print(delta)
    # print(base)

    raiz_1 = (beta - (sqrt(delta)) ) / base
    raiz_2 = (beta + (sqrt(delta)) ) / base

    resultado = [raiz_1, raiz_2]
    return resultado;

try:

    print("Resolveremos uma equação do 2º GRAU de 3 termos")

    a = int(input("DIGITE o 1º termo: "))
    b = int(input("DIGITE o 2º termo: "))
    c = int(input("DIGITE o 3º termo: "))

    termo1 = ""
    termo2 = ""
    termo3 = ""

    termo1 = str(a)

    if (b >= 0):
        termo2 = "+ " + str(b)

    if (c >= 0):
        termo3 = "+ " + str(c)

    print("-----------------------------------------")
    print("Resolvendo a equação: "+termo1+"x² " + termo2 + "x " + termo3 + " = 0")
    print("-----------------------------------------")

    raizes = calcularBaskara(a, b, c);
    print("Resultado: x = " + str(raizes[0]) + " ou x = " + str(raizes[1]))


except:
	print("Não foi possível calcular a equação")

