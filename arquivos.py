"""
arquivo = open("arquivoTeste.txt")

#linhas = arquivo.readlines()

textoCompleto = arquivo.read()

#for linha in linhas:
#	print(linha)


print (textoCompleto)

arquivo.close()
"""

w = open("arquivoTeste2.txt", "a");

w.write("Teste de Escrita \n")

w.close()

#modificaçao branch