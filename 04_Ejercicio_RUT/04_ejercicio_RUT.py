import Utils as U

en_bucle_rut = True
while en_bucle_rut:
    rut = input("Ingrese su rut sin puntos y con guion\n")
    lista_rut = list(rut)
    while not (U.validacion_input_rut(lista_rut)):
        print("Error al ingresar su rut")
        rut = input("Ingrese rut sin puntos y con guion\n")
        lista_rut = list(rut)
    verificador = lista_rut[len(lista_rut) - 1]
    lista_sin_guion = U.funcion_lista_sin_guion(lista_rut)
    es_valido = U.verificacion_de_verificador(lista_sin_guion, verificador)
    if es_valido:
        en_bucle_rut = False
    else:
        print("Rut invalido")

en_bucle_password = True
while en_bucle_password:
    password = input("Ingrese su password\n")
    if len(password) != 10:
        print("Su password debbe ser exatamente de 10 numeros\n")
    else:
        try:
            password = int(password)
            confirmar_password = None
            while confirmar_password != password:
                confirmar_password = input("Confirme su contraseña\n")
                try:
                    confirmar_password = int(confirmar_password)
                    if confirmar_password == password:
                        print("Contraseña creada con exito")
                        en_bucle_password = False
                    else:
                        print("Contraseña no coincide")
                except ValueError:
                    print("Contraseña no coincide")
        except ValueError:
            print("Su contraseña solo debe contener numeros")


# MULTIPLES RUT DE PRUEBAS
"""
Ruts_de_prueba = [
    "17786044-1",  # true
    "16887941-5",  # true
    "6667346-4",  # true
    "12870631-3",  # true
    "15518258-k",  # true
    "21115084-k",  # true
    "123123123-9",  # false
    "23123-9",  # false
    "41231241223-9",  # false
    "239812398123-9",  # false
    "12334-9",  # false
]
"""
