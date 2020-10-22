numbers = [1,2,3,4,5]
results = []

for num in numbers:
    num *= 2
    results.append(num)

results2 = [num * 2 for num in numbers]

print(results)
print(results2)