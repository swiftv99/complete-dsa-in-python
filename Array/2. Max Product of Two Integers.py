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

"""
Time Complexity:
The time complexity of the max_product function is O(n), where n is the length of the input array arr. The reason for this complexity is that the function iterates through the input array once, comparing each element with max_val and second_max_val to find the two largest elements. There are no nested loops or other time-consuming operations, so the time complexity is linear.

Space Complexity:
The space complexity of the max_product function is O(1), which means it uses a constant amount of extra memory regardless of the input size. In this case, the function uses two additional variables, max_val and second_max_val, to store the two largest numbers in the array. No other data structures or memory allocations are required, so the space complexity remains constant regardless of the size of the input array.
"""