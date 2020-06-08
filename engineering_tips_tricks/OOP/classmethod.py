# Tips: Use class method when the method doesn't touch the "self" parameter but still need to access to the class


class Asker():
    def __init__(self, email, password="123456", data={}):
        self.email = email
        self.password = password
        self.data = data

    @classmethod
    def create_asker(cls, email):
        return cls(email)  # == return Asker(email)


asker = Asker.create_asker("huyen@gotitapp.co")
print(asker.email)
print(asker.password)
print(asker.data)
