"""
2D Lists
Given 2D list calculate the sum of diagonal elements.

Example

myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
 
diagonal_sum(myList2D) # 15
"""

def diagonal_sum(matrix):
    result = 0
    for idx in range(len(matrix)):
        result += matrix[idx][idx]
    return result

myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
print(diagonal_sum(myList2D)) # 15

"""
Time complexity:
O(n), where n is the number of rows (or columns) in the matrix. The function iterates through the rows once.

Space complexity:
O(1), as the function only uses a single variable to store the sum (result).
"""