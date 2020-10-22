# filter and map
lista = [10,221,53,31,231,2131,21,312,1,13,4,5]
lista2 = ['Pera','Mika','Zika']

result = [x * 2 if x % 2 == 0 else x + 1 for x in lista if x >= 10]
result2 = [(x,y) for x in lista if x > 55 for y in lista2]
# left side of loop - mapping with condition
# right side of loop - filtering 

print(result) # [20, 222, 54, 32, 232, 2132, 22, 624, 14]
print(result2)
