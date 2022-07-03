set1 = set()

set1.add((1, 1))
set1.add((1, 1))
set1.add((1, 1))
set1.add((1, 1))
set1.add((1, 1))
set1.add((1, 1))
print(set1)

dict1 = {'name': 'tiger'}
print(dict1)
dict1.setdefault('name','beijing')
print(dict1)

set1 = set()
set1 = {1,3,4,2,7,5}
print(set1)

c = compile("print('123')",'','exec')
exec(c)