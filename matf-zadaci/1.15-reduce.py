from functools import reduce

n = int(input('Unesite do kog broja zelite sumu: '))

print(reduce(lambda total,curr: total + curr,range(1,n+1),0))