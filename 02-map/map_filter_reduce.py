from functools import reduce

lista = [1,2,3,4,5,6,7,8,9,10]

print(tuple(map(lambda x: x * 2, lista)))
print(tuple(x * 2 for x in lista)) # Similar to map

print(tuple(filter(lambda x: x % 2 == 0,lista)))
print(tuple(x for x in lista if x % 2 == 0))

print(reduce(lambda total,el: total + el, lista, 0))

