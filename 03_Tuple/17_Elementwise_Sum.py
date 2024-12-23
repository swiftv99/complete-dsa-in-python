"""
Elementwise Sum
Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.

Example
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
output_tuple = tuple_elementwise_sum(tuple1, tuple2)
print(output_tuple)  # Expected output: (5, 7, 9)
"""

def tuple_elementwise_sum(tuple1, tuple2):
    return tuple(sum(pairs) for pairs in zip(tuple1, tuple2))

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
output_tuple = tuple_elementwise_sum(tuple1, tuple2)
print(output_tuple)  # Expected output: (5, 7, 9)

"""
The overall time complexity of the function is O(n) because it iterates through each pair of elements in the input tuples 
once. The overall space complexity is O(n) because the function creates a new tuple with the same length as the input tuples 
to store the element-wise sums.
"""