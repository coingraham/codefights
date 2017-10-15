"""
Given array of integers, find the maximal possible sum of some of its k consecutive elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
arrayMaxConsecutiveSum(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:

2 + 3 = 5;
3 + 5 = 8;
5 + 1 = 6;
1 + 6 = 7.
Thus, the answer is 8.
Input/Output

[time limit] 4000ms (py)
[input] array.integer inputArray

Array of positive integers.

Guaranteed constraints:
3 <= inputArray.length <= 105,
1 <= inputArray[i] <= 1000.

[input] integer k

An integer (not greater than the length of inputArray).

Guaranteed constraints:
1 <= k <= inputArray.length.

[output] integer

The maximal possible sum.
"""

"""
This is the original code I used to solve for this problem but it runs at O(n^2) which is too slow once you start
to utilize larger arrays and larger k values.  The re-work runs at O(n) which is very fast in comparison.
"""
def arrayMaxConsecutiveSum_old(inputArray, k):
    max = 0

    for x in range(0, len(inputArray) - k + 1):
        if sum(inputArray[x:x+k]) > max:
            max = sum(inputArray[x:x+k])

    return max


def arrayMaxConsecutiveSum(inputArray, k):

    max_sum = sum(inputArray[0:k])
    current = sum(inputArray[0:k])

    for x in range(0, len(inputArray) - k):
        right_add = inputArray[k + x]
        left_subtract = inputArray[0 + x]
        new_total = current + right_add - left_subtract

        if new_total > max_sum:
            max_sum = new_total
            current = new_total
        else:
            current = new_total

    return max_sum


if __name__ == '__main__':
    print arrayMaxConsecutiveSum([2, 3, 5, 4, 6], 2)
