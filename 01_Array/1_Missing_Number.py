"""
Missing Number
Write a function to find the missing number in a given integer array of 1 to 100. The function takes to parameter the array 
and the number of elements that needs to be in array.  For example if we want to find missing number from 1 to 6 the second
parameter will be 6.

Example

missing_number([1, 2, 3, 4, 6], 6) # 5
"""

def missing_number(arr, n):
    total = n * (n+1) // 2
    sum_of_array = sum(arr)
    return total - sum_of_array # missing_value

print(missing_number([1, 2, 3, 4, 6], 6))

"""
This function calculates the sum of the first n natural numbers using the arithmetic progression formula and then subtracts
the sum of the numbers in the array to find the missing number. The time complexity of this function is O(n) because it 
iterates through the array once to calculate the sum of its elements.
"""