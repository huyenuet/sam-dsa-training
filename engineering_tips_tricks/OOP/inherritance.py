class User:

    @classmethod
    def login(cls):
        print(cls.__name__ + " logs in successfully")


class Asker(User):
    def ask(self):
        self.login()
        print("post a problem")


# parent class "User" can only access to methods inside "User"
user = User()
user.login()

# child class "Asker" can access to methods inside both "User" and "Asker"
user = Asker()
user.ask()
