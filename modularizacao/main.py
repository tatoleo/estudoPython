import aleatorio as a
import media as m


listaGerada = a.geraListaInteiro(4)

listaGerada.sort()
print (listaGerada)

media = m.calcularMedia(listaGerada)
mediana = m.calcularMediana(listaGerada)
moda = m.calcularModa(listaGerada)

print ("A média é : " + str(media) )
print ("A mediana é : " + str(mediana) )
print ("A moda é : " + str(moda) )
