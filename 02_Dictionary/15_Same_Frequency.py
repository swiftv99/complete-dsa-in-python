"""
Same Frequency
Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

Example:
list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
check_same_frequency(list1, list2)

Output: False
"""

def check_same_frequency(list1, list2):
    def count_elements(lst):
        counter = dict()
        for elem in lst:
            counter[elem] = counter.get(elem, 0) + 1
        return counter
    return count_elements(list1) == count_elements(list2)

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency(list1, list2)) # Output: False

"""
Time complexity:
The overall time complexity of this function is O(n1 + n2 + min(m1, m2)), where n1 and n2 are the lengths of list1 and list2, 
and m1 and m2 are the numbers of distinct elements in list1 and list2, respectively. This is determined by the time complexity
of the count_elements() function and the dictionary comparison.

Space complexity:
The space complexity of this function is O(m1 + m2), where m1 and m2 are the numbers of distinct elements in list1 and list2, 
respectively. This is because the function creates two dictionaries with as many keys as there are distinct elements in the 
input lists.
"""