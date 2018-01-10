"""
Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example

For n = 152, the output should be
deleteDigit(n) = 52;
For n = 1001, the output should be
deleteDigit(n) = 101.
Input/Output

[execution time limit] 4 seconds (py)

[input] integer n

Guaranteed constraints:
10 <= n <= 106.

[output] integer
"""


def deleteDigit(n):
    highest = 0

    number_list = [s for s in str(n)]

    for x in range(0, len(number_list)):

        # Copy the original list
        local_list = number_list[:]

        # Delete the chosen digit
        del local_list[x]

        # Convert the list to a number
        new_number = int(''.join(local_list))

        # Compare and update
        if new_number > highest:
            highest = new_number

    return highest


if __name__ == '__main__':
    print deleteDigit(656)
