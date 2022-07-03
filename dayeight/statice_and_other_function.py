class Father(object):
    public_string = "public_string"
    __private_string = "private_string"

    def __init__(self, car):
        self.car = car

    def rich(self):
        print("父类的rich方法，看看{}".format(self.car))

    def house(self):
        print("父类的house方法")


# f = Father("benz")
# f.rich()
class Son(Father):
    def gift(self):
        print("子类方法,看看{}".format(self.car))


s = Son("benz")
s.gift()
