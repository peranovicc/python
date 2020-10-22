from functools import reduce

inp = '1 2 3 4 5'
inp = inp.split(' ')

print(tuple(map(int, inp)))
# print(tuple(x * 2 for x in lista)) # Similar to map

# print(tuple(filter(lambda x: x % 2 == 0,lista)))
# print(tuple(x for x in lista if x % 2 == 0))

# print(reduce(lambda total,el: total + el, lista, 0))

