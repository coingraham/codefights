"""
Given a sorted array of integers a, find an integer x from a such that the value of

abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)
is the smallest possible (here abs denotes the absolute value).
If there are several possible answers, output the smallest one.

Example

For a = [2, 4, 7], the output should be
absoluteValuesSumMinimization(a) = 4.

Input/Output

[time limit] 4000ms (py)
[input] array.integer a

A non-empty array of integers, sorted in ascending order.

Guaranteed constraints:
1 <= a.length <= 200,
-106 <= a[i] <= 106.

[output] integer
"""


def absoluteValuesSumMinimization(a):

    total = 200 * 10**6
    success = []

    for digit in a:
        list_sum = 0
        for index in range(len(a)):
            list_sum += abs(a[index] - digit)

        if list_sum > total:
            continue

        if total == list_sum:
            success.append(digit)
        else:
            total = list_sum
            del success[:]
            success.append(digit)

    return min(success)

if __name__ == '__main__':
    print absoluteValuesSumMinimization([-1000000, -11, -12, -10, -9, -8, -7, -6, -5, -4, -3,
                                         -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000000])
