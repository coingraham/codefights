"""
Given array of integers, remove each kth element from it.

Example

For inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output should be
extractEachKth(inputArray, k) = [1, 2, 4, 5, 7, 8, 10].

Input/Output

[time limit] 4000ms (py)
[input] array.integer inputArray

Guaranteed constraints:
5 <= inputArray.length <= 15,
-20 <= inputArray[i] <= 20.

[input] integer k

Guaranteed constraints:
1 <= k <= 10.

[output] array.integer

inputArray without elements k - 1, 2k - 1, 3k - 1 etc.
"""


def extractEachKth(inputArray, k):

    for x in range(len(inputArray), 0, -1):
        if x % k == 0:
            inputArray.pop(x - 1)

    return inputArray


def extractEachKth2(x, k):
    # Top answer.  Very interesting.  Took me some time to understand.
    # slice the list [start:end:step].  Start at k-1 (offset for index) and remove every kth step.  So simple.

    del x[k-1::k]
    return x


if __name__ == '__main__':
    print extractEachKth([1, 1, 1, 1, 1], 1)
