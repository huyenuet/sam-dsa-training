class User:
    def login(self, username, password):
        print(f"username: {username}, password: {password}")


class Asker(User):
    def login(self, username, password):
        new_username = username + "_123"
        super().login(new_username, password)


user = User()
user.login("samsam", "123456")

user = Asker()
user.login("samsam", "123456")
