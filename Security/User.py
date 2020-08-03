
class User:

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.state = False

    def getUser(self):
        return self.user

    def getPassword(self):
        return self.password


    def login(self, username, password):
        users = [User("admin","12345"), User("invited","00000")]

        for i in range(len(users)):
            print(users[i])
            if username == users[i].user and password == users[i].password:
                self.state = True
                return self.state
            else:
                return self.state


