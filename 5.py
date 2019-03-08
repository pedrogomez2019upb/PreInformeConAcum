#Conteo de 2 en 2 de 1 a 100
#Primero definimos el contador x y y para que empiecen desde 1
x= 1
y= 1
#Utilizamos While para decirle que imprima los valores siempre y cuando sea menor que 100
while x < 100:
    print("Los valores son: {}.".format(x))
    #Para que haya una sumatoria , x va a ser ese mismo valor mas y
    x=x+y
    #Para que y siga la sumatoria se le agrega un 1 cada vez
    y=y+1
    #Aún asi , cuando ya haya sumado a 5 toca devolverse a 1 entonces
    #definimos un if para que se devuelva a 1
    if y > 5:
        y=1
print("Gracias por utilzar el programa.")
#Desarrollado por Pedro Gómez / ID:000396221