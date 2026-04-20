import Forced_bank_DB as db
bienvenida = "\n///////////////////////////////\n  Bienvenido a Banco estado    \n///////////////////////////////\n"
mi_db = db.users()

print(bienvenida)

user = input("Intregese su nombre de usuario\n").strip()
isAnUser, userIndex = mi_db.getUser(user)
en_bucle = True
while en_bucle == True:
 
 
 if isAnUser == "Usuario no encontrado":
  createUser = int(input("Desea crear un usuario\n 1.si      2.no\n"))
  if createUser == 1:
   newUser = input("Ingrese un nombre\n")
   newPassword = input("Ingrese una contraseña\n")
   newUserMessage = mi_db.addUser(newUser, newPassword)
   print(newUserMessage)
   print("")
   print(bienvenida)
   user = input("Intregese su nombre de usuario\n").strip()
   isAnUser, userIndex = mi_db.getUser(user)
  elif createUser == 2:
   print("Vuelva pronto")
   en_bucle = False

 elif isAnUser == "Usuario encontrado":
  password = input("Ingrese su contraseña\n").strip()
  validate = mi_db.comparePassword(user, password)

  for i in range (4):
   if validate == True:
    break
   elif validate == False :
    password = input("Contraseña incorrecta, intente nuevamente\n").strip()
    validate = mi_db.comparePassword(user, password)

  if validate == True: 
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


    
   










