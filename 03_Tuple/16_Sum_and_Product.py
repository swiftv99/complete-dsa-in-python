"""
Sum and Product
Write a function that calculates the sum and product of all elements in a tuple of numbers.

Example
input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)  # Expected output: 10, 24
"""

def sum_product(input_tuple):
    sum_result = 0
    product_result = 1
    for elem in input_tuple:
        sum_result += elem
        product_result *= elem
    return sum_result, product_result


input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)  # Expected output: 10, 24

"""
Overall time complexity of the function is O(n) because the loop iterates through each element in the tuple once. The rest of
the operations have constant time complexity O(1). The overall Space complexityis O(1) because the function uses a constant amount of additional memory to store the sum and product, regardless of the size of the input tuple.
"""