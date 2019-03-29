# calcular a média, a mediana e a moda
from statistics import *

def calcularMedia (lista):
	#mean(lista)
	media = sum(lista)/float(len(lista))
	return round(media, 2)



def calcularMediana (lista):
	#return median(lista)
	lista_ordenada = sorted(lista)
	tamanho = len(lista_ordenada)

	if ((tamanho % 2) == 0):
		mediana = (lista_ordenada[int(tamanho/2)-1] + lista_ordenada[int(tamanho/2)])/2
	else:
		mediana = lista_ordenada[(tamanho//2)]

	return mediana


def calcularModa (lista):

	lista_somas = {}

	for item in lista:
		if item not in lista_somas:
			lista_somas[item] = 1
		else:
			lista_somas[item] += 1

	maior_repeticao = max(lista_somas.values())

	for indice in lista_somas:
		if lista_somas[indice] == maior_repeticao:
			moda = indice

	return moda;