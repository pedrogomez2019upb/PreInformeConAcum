#Algoritmo que imprima los números pares entre 1 y 30
#Primero vamos a crear un contador desde 0
contar_pares = 0
#Creamos una condicional for para que este en rango entre 1 y 30
for x in range (1,30):
    #Vamos a poner una condicional if para poner la condicion de los números pares
    if x%2 == 0:
        #Simplemente imprimimos el resultado
        print("Los números pares entre 1 y 30 son: {}".format(x))

#Desarrollado por Pedro Gómez / ID:000396221