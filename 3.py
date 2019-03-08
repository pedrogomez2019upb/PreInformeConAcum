#Algoritmo que lea 5 números y lea el mayor de ellos
#Primero vamos a poner una condicional for para que los lea en el rango de 0 y 5
for i in range(0,5):
    #Se crea la variable que va a recibir los valores a evaular.
    x = float(input("Por favor ingrese el número a evaluar: "))
    #Ponemos un if y then para que revise la cantidad de números
    if i ==0:
        mayor=x
    else:
        if x>mayor:
            mayor=x
print("El número mayor es: {} ".format(mayor))
#Desarrollado por Pedro Gómez / ID:000396221
    