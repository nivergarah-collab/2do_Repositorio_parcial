
def Validacion_numerica(rango, eleccion):
    en_bucle = True
    while en_bucle == True:
     try: 
        if eleccion in range(rango +1): 
            return eleccion
        else:
            eleccion = int(input("Ingrese un valor valido\n"))
     except ValueError:
        eleccion = int(input("Ingrese un valor valido\n"))
      
