"""
Rotate Matrix / Image - LeetCode 48
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
"""

def rotate(matrix):
    length = len(matrix)
    # Flip the matrix upside down.
    for r_idx in range(length//2):
        matrix[r_idx], matrix[length - r_idx - 1] = matrix[length - r_idx - 1], matrix[r_idx]
    
    # Transpose the matrix
    for r_idx in range(length):
        for c_idx in range(r_idx + 1, length):
            matrix[r_idx][c_idx], matrix[c_idx][r_idx] = matrix[c_idx][r_idx], matrix[r_idx][c_idx]

    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix)) # Output: [[7,4,1],[8,5,2],[9,6,3]]

"""
The time complexity of this code is O(n^2), as both the transpose and reverse steps involve nested loops that iterate over all 
the elements in the matrix. The space complexity is O(1), as the rotation is performed in-place without allocating any 
additional data structures.
"""