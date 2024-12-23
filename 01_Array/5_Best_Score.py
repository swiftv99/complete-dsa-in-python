"""
Best Score
Given a list, write a function to get first, second best scores from the list.

List may contain duplicates.

Example

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
first_second(myList) # 90 87
"""

def first_second(my_list):
    first_best = second_best = 0
    
    for element in my_list:
        if element > first_best:
            second_best = first_best
            first_best = element
        elif element > second_best and element != first_best:
            second_best = first_best
            
    return first_best, second_best

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
print(first_second(myList)) # 90 87

"""
Time complexity:
The function iterates through the list my_list once, with each iteration taking constant time O(1) to perform comparisons and
updates. Since there are n elements in the list, the overall time complexity of the function is O(n).

Space complexity:
The function uses a constant amount of additional space to store the variables first_best and second_best. There are no other
data structures or variables created that depend on the size of the input list. Therefore, the space complexity is O(1), as it
remains constant regardless of the input size.
"""