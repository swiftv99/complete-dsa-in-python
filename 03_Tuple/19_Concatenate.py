"""
Concatenate
Write a function that takes a tuple of strings and concatenates them, separating each string with a space.

Example
input_tuple = ('Hello', 'World', 'from', 'Python')
output_string = concatenate_strings(input_tuple)
print(output_string)  # Expected output: 'Hello World from Python'
"""

def concatenate_strings(input_tuple):
    return " ".join(input_tuple)

input_tuple = ('Hello', 'World', 'from', 'Python')
output_string = concatenate_strings(input_tuple)
print(output_string)  # Expected output: 'Hello World from Python'

"""
The overall time complexity of the function is O(n) because it iterates through the strings in the input tuple once to create 
a new concatenated string. The overall space complexity is O(n) because it creates a new concatenated string with the length 
equal to the sum of the lengths of the strings in the input tuple plus the spaces in between.
"""