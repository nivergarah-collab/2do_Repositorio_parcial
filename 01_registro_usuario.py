
dbUsers= ["Mario", "Juan", "Luis"]
dbPass=["1", "2", "3"]


print("////////////////////////////////////")
print("// Bievenido a la aplicacion Duoc //")
print("////////////////////////////////////")



en_bucle = True
while en_bucle == True:
 
 opcion=input(" 1.Ingresar 2.Registrarse\n\n")

 if opcion == "1":
  
  nombre=input("Ingresa tu nombre\n")
  password =input("Ingresa tu contraseña\n")

  try:
    indice_auxiliar = dbUsers.index(nombre)
    if password == dbPass[indice_auxiliar]:
      print("Usuario ingresado exitosamente\n")
      en_bucle = False
    else: 
      print("Password error\n")
  
  except ValueError:
   print("Usuario inexistente\n")
    





 elif opcion =="2":
  print("registrate")
  nuevoUsuario=input("ingresa el nombre de usuario\n")
  nuevaContraseña=input("ingresa contraseña\n")
  validacionContraseña=input("ingresa nuevamente\n")
  while nuevaContraseña != validacionContraseña: 
   validacionContraseña =input("las contraseñas no coinciden\n") 
  dbUsers.append(nuevoUsuario) 
  dbPass.append(nuevaContraseña)
  print(dbUsers)

 else: 
  opcion = input("Ingrese una opcion valida\n")




  









