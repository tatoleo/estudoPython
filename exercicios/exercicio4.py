# programa que ordena uma lista de 3 elementos

import random

def geraListaInteiro (tamanho):
	lista = []
	for i in range(tamanho):
		lista.append(random.randint(0, tamanho*5))
	return lista


lista = geraListaInteiro(3)

print(lista)

lista_ordenada = sorted(lista)

print(lista_ordenada)


