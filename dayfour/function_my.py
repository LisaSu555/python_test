
count = 0


def function1():
    global count1
    count1 = 1
    count = 6
    print("f1 has been called")


function1()

print("the first count is %d" % (count))


def function2():
    count = 2
    print("count1 is %d" % count1)
    print("f2 has been called")


function2()


print("the second count is %d" % (count))
