#from DB.LectorJSON import LectorJSON


class User:

    def __init__(self, user, password):
        """self.rol = rol"""
        self.user = user
        self.password = password
        self.state = False
        #self.getListUser()

    def getUser(self):
        return self.user

    def getPassword(self):
        return self.password

    """def getListUser(self):
        u = []
        for user in LectorJSON().reader():
            listUser = User(user.get('username'), user.get('password'))
            # print(user)
            #print(listUser.password)
            u.append(listUser)
        # print(u)
        return u"""

    def login(self, username, password, list):
        #users = [User( "admin","12345"), User( "invited","00000")]
        #print(list)
        for a in list:
            print(a.user+" "+ a.password )

        for dataUser in list:
            #print(users[i])
            if username == dataUser.user and password == dataUser.password:
                self.state = True

        return self.state


