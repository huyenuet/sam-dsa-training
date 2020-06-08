# A double underscore prefix causes the Python interpreter
# to rewrite the attribute name
# A name prefixed with an underscore should be treated as a non-public part
# However, this is just a convention, not a built-in Python feature


class User:
    def __init__(self):
        self.__id = 1
        self._name = "Hello world!"

    def get_id(self):
        return self.__id


user = User()
print(user.get_id())  # 1
print(user._User__id)  # 1
print(user._name)  # Hello world!
print(user.__id)  # NameError: "name '__id' is not defined"
