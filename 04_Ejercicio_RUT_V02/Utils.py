# RUT
def validacion_input_rut(lista_rut):
    lista_local = lista_rut.copy()
    if "-" in lista_local:
        lista_local.remove("-")
        if "k" in lista_local:
            lista_local.remove("k")
        string_rut = "".join(lista_local)
        try:
            string_rut = int(string_rut)
            return True
        except ValueError:
            return False
    else:
        return False


def funcion_lista_sin_guion(lista_rut):
    lista_sin_guion = lista_rut.copy()
    lista_sin_guion.pop()
    lista_sin_guion.pop()
    return lista_sin_guion


def verificacion_de_verificador(lista_sin_guion, verificador):
    lista_sin_guion.reverse()
    acumulador = 0
    multiplicador = 2
    for i in lista_sin_guion:
        acumulador = (int(i) * multiplicador) + acumulador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2
    comprobador_verificador = 11 - (acumulador % 11)
    if comprobador_verificador == 10:
        comprobador_verificador = "k"
    if str(comprobador_verificador) == verificador:
        verificado = True
    else:
        verificado = False
    return verificado


def Validacion_numerica(rango, eleccion):
    en_bucle = True
    while en_bucle:
        try:
            if int(eleccion)-1  in range(rango): 
                eleccion = int(eleccion)
                return eleccion + 1
            else:
                eleccion = input("Ingrese un valor valido\n")
        except ValueError:
            eleccion = input("Ingrese un valor valido\n")


# Password
