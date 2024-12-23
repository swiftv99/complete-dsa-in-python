"""
Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example :
Input: nums = [1,2,3,1]
Output: true
Hint: Use sets
"""

def contains_duplicate(nums):
    return len(nums) != len(set(nums))

nums = [1,2,3,1]
print(contains_duplicate(nums)) # Output: true

"""
Since the set() method runs n times, the overall time complexity of the contains_duplicate function is O(n), where n is the
length of the input array nums. O(n), where n is the length of the input array nums, as in the worst case, the set seen may 
store all unique elements of the array.
"""