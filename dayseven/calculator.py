class Calculator(object):

    def __init__(self, one=10, two=2):
        self.one = one
        self.two = two

    def add(self):
        return self.one + self.two

    def jian(self):
        return self.one - self.two

    def mul(self):
        return self.one * self.two

    def dev(self):
        return self.one / self.two


c = Calculator()
print(c.add())
print(c.jian())
print(c.mul())
print(c.dev())