class users:
    def __init__(self):
        self.usersDb = [
            {"user": "pedro",
             "password":"123"},
            {"user": "juan",
             "password":"231"},
            {"user": "diego",
             "password":"312"},
        ]
        self.currentUserName = None
        self.currentUserPassword = None

    def getUser(self, username):
        for i, user_dict in enumerate(self.usersDb):  
            if user_dict["user"] == username:
                self.currentUserName = user_dict["user"]
                self.currentUserPassword = user_dict["password"]
                return "Usuario encontrado", user_dict, i
        return "Usuario no encontrado"
    
    def comparePassword(self, username, password):
        resultado = self.getUser(username)
        if resultado[0] == "Usuario encontrado":
            return resultado[1]["password"] == password  # Retorna True/False
        return resultado[0]  # Retorna "Usuario no encontrado"
    
    def addUser(self, newUser, newpassword):
        try:
            self.usersDb.append({"user": newUser, "password": newpassword})
            return "User added"
        except:
            return "Unexpected error adding user"
    
    def deleteUser(self, username):
        resultado = self.getUser(username)
        if resultado[0] == "Usuario encontrado":
            try:
                self.usersDb.remove(resultado[1])  # resultado[1] es el dict
                return "usuario removido exitosamente"
            except:
                return "unexpected error in delete"
        return resultado[0] if isinstance(resultado, str) else "Usuario no encontrado"