"""
Max Product of Two Integers
Find the maximum product of two integers in an array where all elements are positive.

Example

arr = [1, 7, 3, 4, 9, 5] 
max_product(arr) # Output: 63 (9*7)
"""

def max_product(arr):
    max_val = second_max_val = 0
    
    for elem in arr:
        if elem > max_val:
            second_max_val = max_val
            max_val = elem
        elif elem > second_max_val:
            second_max_val = elem
            
    return max_val * second_max_val

arr = [1, 7, 3, 4, 9, 5] 
print(max_product(arr)) # Output: 63 (9*7)