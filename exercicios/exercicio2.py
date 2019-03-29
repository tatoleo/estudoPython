# programa que recebe 2 notas e se a média é maior que 6 é aprovado

try:

    n1 = float(input("DIGITE nota 1: "))
    n2 = float(input("DIGITE nota 2: "))

    media = (n1 + n2) /2

    aprovado = False
    if (float(media) >= 6):
        aprovado = True


    print("Média: " + str(media))
    if (aprovado) :
        print("Você está aprovado")
    else:
        print("Você está reprovado")

except:
	print("Não foi possível verificar a nota")
