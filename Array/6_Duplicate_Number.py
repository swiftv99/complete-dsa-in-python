"""
Duplicate Number
Write a function to remove the duplicate numbers on given integer array/list.

Example

remove_duplicates([1, 1, 2, 2, 3, 4, 5])
Output : [1, 2, 3, 4, 5]
"""

def remove_duplicates(arr):
    seen_set = set()
    unique_list = list()
    for elem in arr:
        if elem not in seen_set:
            seen_set.add(elem)
            unique_list.append(elem)
    return unique_list

print(remove_duplicates([1, 1, 2, 2, 3, 4, 5])) # Output : [1, 2, 3, 4, 5]

"""
Time complexity:
The loop iterates through the entire list once, and the set operations (lookup, add) inside the loop have an average time
complexity of O(1). Therefore, the overall time complexity is O(n).

Space complexity:
O(n), as we're using additional data structures (list and set) to store unique elements.
"""