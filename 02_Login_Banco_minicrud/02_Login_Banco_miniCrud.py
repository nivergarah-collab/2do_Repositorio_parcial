import Forced_bank_DB as db
import Utils as U

bienvenida = "\n///////////////////////////////\n  Bienvenido a Banco estado    \n///////////////////////////////\n"
mi_db = db.users()


en_bucle = True
while en_bucle:
    print(bienvenida)
    user = input("Intregese su nombre de usuario\n").strip()
    isAnUser, userIndex = mi_db.getUser(user)

    if isAnUser == "Usuario no encontrado":
        createUser = int(input("Desea crear un usuario\n 1.si      2.no\n"))
        U.Validacion_numerica(2, createUser)

        if createUser == 1:
            addUsermesagge = mi_db.addUserV2()
            print(addUsermesagge)

        elif createUser == 2:
            print("Vuelva pronto")
            en_bucle = False

    elif isAnUser == "Usuario encontrado":
        password = input("Ingrese su contraseña\n").strip()
        validate = mi_db.comparePassword(user, password)

        for i in range(4):
            if validate:
                break
            elif validate:
                password = input("Contraseña incorrecta, intente nuevamente\n").strip()
                validate = mi_db.comparePassword(user, password)

        if validate:
            print("#############################")
            print(f"   Bienvenido {user}")
            print("    Login exitoso")
            print("#############################")
            en_bucle = False
        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("   Porfavor comuniquese con nuestro call center")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            en_bucle = False
