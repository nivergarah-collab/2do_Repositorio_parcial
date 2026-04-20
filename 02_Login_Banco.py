print("///////////////////////////////")
print("  Bienvenido a Banco estado\n")
print("///////////////////////////////")

user = input("Intregese su nombre de usuario\n").strip()
true_password = "12345"
password = input("Ingrese su contraseña\n").strip()


for i in range (3):
 if password != true_password:
   password = input("Contraseña incorrecta, intente nuevamente\n")
 else: 
   break

if password == true_password: 
 print(f"bienvenido {user}")
 print("Login exitoso")
else: 
 print("Porfavor comuniquese con nuestro call center")






