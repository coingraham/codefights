"""
Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal
to product. If there is no such integer, return -1 instead.

Example

For product = 12, the output should be
digitsProduct(product) = 26;
For product = 19, the output should be
digitsProduct(product) = -1.
Input/Output

[execution time limit] 4 seconds (py)

[input] integer product

Guaranteed constraints:
0 <= product <= 600.

[output] integer
"""

def digitsProduct(product):

    for nums in range(1, 99999):
        number_list = [int(d) for d in str(nums)]
        test = reduce(lambda x, y: x*y, number_list)
        if test == product:
            return nums

    return -1


if __name__ == '__main__':
    print digitsProduct(12)
