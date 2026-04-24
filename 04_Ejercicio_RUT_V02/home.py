import UserManager as U_Man
import assets as a
import Utils as U

DB = U_Man.users()


print(a.Bienvenida)
eleccion01 = input(a.Menu01)
eleccion01 = U.Validacion_numerica(2, eleccion01)

if eleccion01 == 1:
    #Ingreso Rut
    rut = input("Ingrese su rut\n")
    findedUser, index= DB.getUser(rut)
    print(findedUser)
    while findedUser != "Usuario encontrado":
        print("Usuario no registrado")
        rut = input("Intente Nuevamente\n")
        findedUser=DB.getUser(rut)
    
    password = input("Ingrese su password\n")
    validatedPassword = DB.comparePassword(rut, password)
    counter = 5
    while not(validatedPassword) and counter > 0:
        password = input(f"Passord incorrecto\nLe quedan {counter -1}\n")
        validatedPassword = DB.comparePassword(rut, password)
        counter -= 1
    if counter == 0: 
        print("Contraseña incorrecta, saliendo de sistema")
    else: 
        print("Bienvenido, Registro exitoso")
else: 
    en_bucle_rut = True
    while en_bucle_rut:
     rut = input("Ingrese su rut sin puntos y con guion\n")
     findedUser, index = DB.getUser(rut)
     while findedUser == "Usuario encontrado":
      print("Usuario ya creado")
      rut = input("Ingrese un nuevo rut\n")
      findedUser, index = DB.getUser(rut)
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
     password = input("Ingrese password\n")
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
                        print("Usuario creado con exito")
                        en_bucle_password = False
                    else:
                        print("Contraseña no coincide")
                except ValueError:
                    print("Contraseña no coincide")
        except ValueError:
            print("Su contraseña solo debe contener numeros")

        DB.addUserV2(rut, password)
    
    

    



    #Ingreso contraseña


    






"""
usuarioEncontrado = DB.getUser("17786044-1")
comparePassword  = DB.comparePassword("17786044-1","0123456789")
addUsser = DB.addUserV2()

print(usuarioEncontrado)
print(comparePassword)

"""