# The sum of all odd integers from a through b, inclusively.
from functools import reduce

a = 4301
b = 8596

print(reduce(lambda total,el: total + el if el % 2 != 0 else total,range(a,b+1),0))
