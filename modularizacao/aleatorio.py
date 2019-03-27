import random

def geraListaInteiro (tamanho):
	lista = []
	for i in range(tamanho):
		lista.append(random.randint(0,tamanho))
	return lista