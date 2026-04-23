class users:
    def __init__(self):
        self.usersDb = [
            {"user": "pedro", "password": "123"},
            {"user": "juan", "password": "231"},
            {"user": "diego", "password": "312"},
        ]

    def getUser(self, username):
        for i in self.usersDb:
            if i["user"] == username:
                self.currentUserName = i["user"]
                self.currentUserPassword = i["password"]
                getUserMessage = "Usuario encontrado"
                index = self.usersDb.index(i)
                # print("index: ", index)
                return getUserMessage, index

        getUserMessage = "Usuario no encontrado"
        return getUserMessage, None

    def comparePassword(self, username, password):
        catchedMessage, user_index = self.getUser(username)
        # print(self.currentUserName)
        # print(self.currentUserPassword)
        # print(catchedMessage)
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

    def addUserV2(self):
        try:
            newUser = input("Ingrese un nombre\n")
            en_bucle = True
            while en_bucle:
                message, userIndex = self.getUser(newUser)
                if "Usuario encontrado" == message:
                    newUser = input("Nombre ya opcupado\nIngrese Otro\n")
                else:
                    en_bucle = False

            newPassword = input("Ingrese una contraseña\n")
            newAddition = {"user": newUser, "password": newPassword}
            self.usersDb.append(newAddition)
            addUserMessage = "User added"
            return addUserMessage
        except:
            addUserMessage = "Unespected error adding user"
            return addUserMessage

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
    def addUser(self, newUser, newpassword):
        try:
         newAddition = {"user": newUser, 
                       "password": newpassword}
         self.usersDb.append(newAddition)
         addUserMessage = "User added"
         return addUserMessage
        except:
           addUserMessage = "Unespected error adding user"
           return addUserMessage
        """
