"""
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example

sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
"""

def sort_array(arr):
    odd = list(filter(lambda el: el % 2,arr)) # Extract odd numbers in order
    odd.sort() # Sorting odd numbers
   
    # Mapping each number in original array (if odd take first from odd array, else do nothing (even numbers stay the same))
    return list(map(lambda el: odd.pop(0) if el % 2 else el,arr)) 

print(sort_array([2,1,33,5,4,6,3,2]))