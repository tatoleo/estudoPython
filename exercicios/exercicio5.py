# programa que receba 2 numeros e um sinal e execute a operação
import operator

operator_dict = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

try:

    fator1 = float(input("DIGITE um número: "))
    fator2 = float(input("DIGITE outro número: "))

    operacao = input("DIGITE uma operação (+, -, *): ")

    resultado = operator_dict[operacao](fator1, fator2)
    print(str(fator1) + " " + str(operacao) + " " + str(fator2) + " = " + str(resultado))


except:
	print("Não foi possível calcular a equação")

