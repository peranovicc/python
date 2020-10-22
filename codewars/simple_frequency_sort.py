"""
In this Kata, you will sort elements in an array by decreasing frequency of elements.
If two elements have the same frequency, sort them by increasing value.

solve([2,3,5,3,7,9,5,3,7]) = [3,3,3,5,5,7,7,2,9]
"""
from functools import cmp_to_key

def solve(arr):
    freq = {}
    for el in arr:
        if el in freq.keys():
            freq[el] += 1
        else:
            freq[el] = 1
    
    # sorted is immutable version of sort (returns new array with sorted values)
    # cmp_to_key converts element of an array to K class, whose values are "sorted" according to given function (our lambda)
    return sorted(arr,key=cmp_to_key(lambda a,b: freq[b] - freq[a] or a - b))

print(solve([6,1,1,6,6,2,3,3,3,55,2,6,1,1,2,6,6,1]))

