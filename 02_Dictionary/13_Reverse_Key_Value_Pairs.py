"""
Reverse Key-Value Pairs
Define a function which takes as a parameter dictionary and returns a dictionary in which every the key-value pairs are reversed.

Example:
my_dict = {'a': 1, 'b': 2, 'c': 3}
reverse_dict(my_dict)

Output: {1: 'a', 2: 'b', 3: 'c'}
"""

def reverse_dict(my_dict):
    return {value: key for key, value in my_dict.items()}

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(reverse_dict(my_dict)) # Output: {1: 'a', 2: 'b', 3: 'c'}

"""
Time complexity:
The overall time complexity of this function is O(n), where n is the number of elements in the dictionary my_dict. This is 
determined by the dictionary comprehension, which iterates through all the key-value pairs in the input dictionary.

Space complexity:
The space complexity of this function is O(n), where n is the number of elements in the dictionary my_dict. This is because the 
function creates a new dictionary with the same number of elements as the input dictionary but with reversed key-value pairs.
"""