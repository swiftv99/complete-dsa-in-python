"""
Key with the Highest Value
Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

Example:
my_dict = {'a': 5, 'b': 9, 'c': 2}
max_value_key(my_dict))
Output: b
"""

def max_value_key(my_dict):    
    max_value = float('-inf')
    result_key = None
    for current_key, current_value in my_dict.items():
        if current_value > max_value:
            max_value = current_value
            result_key = current_key
    return result_key

# def max_value_key(my_dict):
#     return max(my_dict, key=my_dict.get)

my_dict = {'a': 5, 'b': 9, 'c': 2}
print(max_value_key(my_dict)) # Output: b

"""
Time Complexity:
The overall time complexity of the max_value_key function is O(n), where n is the number of elements in the dictionary my_dict.
The function iterates through all the key-value pairs in my_dict using the for loop.
Each iteration involves a comparison (if current_value > max_value) and a potential assignment, both of which are O(1) perations.

Space Complexity:
The space complexity of the max_value_key function is O(1).
The function uses a constant amount of extra space to store two variables: max_value (to track the maximum value) and 
result_key (to track the corresponding key). No additional data structures or intermediate results are created during execution.
"""