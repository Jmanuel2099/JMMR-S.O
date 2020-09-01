import json
from Security.User import User

class LectorJSON:

    def reader(self):
        with open('DB/proyectoJSON.json') as content:
            data = json.load(content)
            user = self.getUser(data.get('User'))
            #user = data.get('User')
            #for a in user:
             #   print(a.password)

        return user

    def getUser(self,lista):
        u =[]
        for user in lista:
            listUser= User(user.get('username'), user.get('password'))
            #print(user)
            #print(listUser.password)
            u.append(listUser)
        #print(u)
        return u