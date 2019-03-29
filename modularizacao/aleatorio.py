import random

def geraListaInteiro (tamanho):
	lista = []
	for i in range(tamanho*5):
		lista.append(random.randint(0, tamanho))
	return lista