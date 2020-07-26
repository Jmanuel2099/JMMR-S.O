class User:

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.state = False

    def login(self, username, password):
        user = "JMMR2099"
        passw = "1234567890"

        if username == user and password == passw:
            self.state = True
            return self.state
        else:
            return self.state


