import re


def main():
    content = 'Hello, I am Jerry, from Chongqing, a montain city, nice to meet you……'
    regex = re.compile('\w*a\w*')
    x = regex.findall(content)
    print(x)


def one():
    str = "aabkkbaaabkkks"
    c = re.findall("a{2}b", str)
    print(c)


if __name__ == '__main__':
    one()


