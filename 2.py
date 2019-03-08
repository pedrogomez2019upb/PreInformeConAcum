#Imprimir los primeros 10 números pares entre 1 y 30
#Primero que todo nos toca hacer un contador para los números pares que empiece en 0.
contar_pares = 0
#Creamos una condicional para el rango de for
for x in range (1,30):
    #Creamos un if con un and para que solo imprima los primeros 10
    if (x%2== 0 and x<21):
        #Imprimimos el resultado
        print("Los 10 primeros números pares entre 1 y 30 son: {}".format(x))
#Desarrollado por Pedro Gómez / ID:000396221