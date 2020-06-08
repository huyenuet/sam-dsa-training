class Asker:
    def __init__(self, eg):
        self.__eg = eg

    @property
    def eg(self):
        return self.__eg

    @eg.setter
    def eg(self, eg):
        if eg < 8:
            self.__eg = 8
        elif eg > 40:
            self.__eg = 40
        else:
            self.__eg = eg


user = Asker(2)
user.eg = 22
print(user.eg)

user.eg = 7
print(user.eg)

user.eg = 49
print(user.eg)
