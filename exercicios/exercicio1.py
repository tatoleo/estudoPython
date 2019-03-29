# programa que recebe uma idade e diga se é maior ou menor de idade

idade = input("DIGITE sua idade: ")

try:
    if (int(idade) >= 18):
        print("Você é maior de idade")
    elif ( int(idade) > 0):
        print("Você é menor de idade")
    else:
        print("Idade Inválida")

except:
	print("Não foi possível verificar a idade")

