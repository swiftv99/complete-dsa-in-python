"""
Diagonal
Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.

Example
input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
output_tuple = get_diagonal(input_tuple)
print(output_tuple)  # Expected output: (1, 5, 9)
"""

def get_diagonal(tup):
    return tuple(tup[idx][idx] for idx in range(len(tup)))

input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
output_tuple = get_diagonal(input_tuple)
print(output_tuple)  # Expected output: (1, 5, 9)

"""
The overall time complexity of the function is O(n) because it iterates through the indices of the input tuple once to create
a new tuple with the diagonal elements. The overall space complexity is O(n) because it creates a new tuple containing the 
diagonal elements, which has a length equal to the length of the input tuple.
"""