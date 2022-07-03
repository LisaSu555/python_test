class Man(object):
    u = 80

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(nnn):
        print("i can say")
        return "lll"


class Teacher(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(mmm):
        print("t i can say")
        return "ttt"


t = Teacher("tiger",18)
a1 = t.age # 调用属性
a2 = t.name # 调用属性
t.say() # 调用方法


