"""
Common Elements
Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.

Example
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)  # Expected output: (4, 5)
"""

def common_elements(tuple1, tuple2):
    return tuple(set(tuple1).intersection(set(tuple2)))

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)  # Expected output: (4, 5)

"""
Time and Space Complexity
Therefore, the overall time complexity of the function is O(n), and the overall space complexity is also O(n), where n is the 
length of the input tuples.
"""