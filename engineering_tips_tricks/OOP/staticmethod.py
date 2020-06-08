# Tips: Use static method when the method doesn't touch the "self" parameter or the class itself.
# Example: a Class has 2 methods that need to use a common method


class Dummy:
    @staticmethod
    def increase(number):
        return number + 1

    def method_1(self, x):
        return self.increase(x)

    def method_2(self, y):
        return self.increase(-y)


print(Dummy().method_1(4))
print(Dummy().method_2(4))
