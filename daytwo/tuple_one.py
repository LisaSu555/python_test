

a = ()
print(type(a))

b = list(a)
print(type(b))

b.append(1)
a = tuple(b)
print(type(a))
print(a)