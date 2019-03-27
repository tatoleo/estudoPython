# calcular a média, a mediana e a moda
from statistics import *

def calcularMedia (lista):
	#mean(lista)
	media = sum(lista)/float(len(lista))
	return media



def calcularMediana (lista):
	return median(lista)
	"""
	soma = 0;
	tamanho = len(lista)
	for item in lista:
		soma = soma + item

	media = soma/tamanho
	return media
	"""

def calcularModa (lista):
	return mode(lista)
	"""
	soma = 0;
	tamanho = len(lista)
	for item in lista:
		soma = soma + item

	media = soma/tamanho
	return media
	"""