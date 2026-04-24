import json

class users:
    def __init__(self):
      self.path = "04_Ejercicio_RUT_V02/DB.json"
      with open(self.path, "r") as userDb:
       self.usuarios = json.load(userDb)
       print(self.usuarios)

    def getUser(self, username):
        #print(username)
        for i in self.usuarios:  
          if i["rut"] == username:
              self.currentUserName = i["rut"]
              self.currentUserPassword = i["password"]
              self.currentUserName = i["name"]
              getUserMessage = "Usuario encontrado"
              index = self.usuarios.index(i)
              return getUserMessage, index
        getUserMessage = "Usuario no encontrado"
        return getUserMessage, None
    
    def comparePassword(self, rut, password):
       catchedMessage,user_index = self.getUser(rut)
       #print(self.currentUserName)
       #print(self.currentUserPassword)
       #print(catchedMessage)
       if catchedMessage == "Usuario encontrado":
          if self.currentUserPassword == password:
             comparePasswordMessage = True
             return comparePasswordMessage
          else:
             comparePasswordMessage = False
             return comparePasswordMessage
       elif catchedMessage == "Usuario no encontrado":
          return catchedMessage
       else:
          comparePasswordMessage = "Unespected error in comparison"
          return comparePasswordMessage


    def addUserV2(self, newRut, newPassword):
             newRut = newRut
             newPassword = newPassword
             newAddition = {"rut": newRut, 
                             "name": "No solucionado",
                            "password": newPassword}
             self.usuarios.append(newAddition)
             with open(self.path, "w") as userDb:
              json.dump(self.usuarios, userDb, indent=4)
             addUserMessage = "User added"
             return addUserMessage

"""
# EN DESARROLLO
    
    def deleteUser(self, username):
       catchedMessage, userIndex = self.getUser(username)
       if catchedMessage == "Usuario encontrado":
          try:
           self.usersDb.remove(userIndex)
           deleteUserMessage = "usuario removido exitosamente"
           return deleteUserMessage
          except: 
             deleteUserMessage = "unespected error in delate"
             return deleteUserMessage
       elif catchedMessage == "Usuario no encontrado":
          return catchedMessage 
       else:
             deleteUserMessage = "unespected error in delate"
             return deleteUserMessage
"""