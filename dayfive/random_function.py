import random
import math


def random_my():
    base = 50
    a = random.random()
    num = math.floor(base * a + 50)
    print(num)
    print(random.randint(1, 88))


if __name__ == '__main__':
    random_my()

