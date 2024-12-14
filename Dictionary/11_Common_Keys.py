"""
Common Keys
Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

Example:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merge_dicts(dict1, dict2)

Output:
{'a': 1, 'b': 5, 'c': 7, 'd': 5}
"""

def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key in dict2:
        result[key] = dict1.get(key, 0) + dict2[key]
    return result

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts(dict1, dict2)) # {'a': 1, 'b': 5, 'c': 7, 'd': 5}

"""
Time complexity:
The overall time complexity of this function is O(n + m), where n is the number of elements in dict1 and m is the number of elements in dict2. The copy() method takes O(n) time, and the loop iterates m times with O(1) operations inside the loop.

Space complexity:
The space complexity of this function is O(n + m) in the worst case, where all keys in dict1 and dict2 are distinct, and the merged dictionary has n + m elements. In the best case, where dict1 and dict2 have the same keys, the space complexity is O(n) (or O(m), whichever is larger), as the merged dictionary has the same number of elements as the input dictionaries.
"""