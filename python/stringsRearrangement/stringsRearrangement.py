"""
Given an array of equal-length strings, check if it is possible to rearrange the strings in such a way that after the rearrangement the strings at consecutive positions would differ by exactly one character.

Example

For inputArray = ["aba", "bbb", "bab"], the output should be
stringsRearrangement(inputArray) = false;

All rearrangements don't satisfy the description condition.

For inputArray = ["ab", "bb", "aa"], the output should be
stringsRearrangement(inputArray) = true.

Strings can be rearranged in the following way: "aa", "ab", "bb".
Input/Output

[time limit] 4000ms (py)
[input] array.string inputArray

A non-empty array of strings of lowercase letters.

Guaranteed constraints:
2 <= inputArray.length <= 10,
1 <= inputArray[i].length <= 15.

[output] boolean
"""

import itertools
import time
start_time = time.time()


def stringsRearrangement(inputArray):

    print("--- Beginning %s seconds ---" % (time.time() - start_time))

    found = False

    # Moving this iteration to it's own variable solved my performance issues.
    master_list = list(itertools.permutations(inputArray, len(inputArray)))


    print("--- Master list loop %s seconds ---" % (time.time() - start_time))
    for compare_list in master_list:

        #print("--- Inside master list skip %s seconds ---" % (time.time() - start_time))
        if found:
            return found

        for x in range(len(compare_list)-1):
            same = 0
            for y in range(len(compare_list[x])):
                if list(compare_list[x])[y] != list(compare_list[x + 1])[y]:
                    same += 1

            if same == 1:
                found = True
            else:
                found = False
                break


    print("--- Complete %s seconds ---" % (time.time() - start_time))
    return found


if __name__ == '__main__':
    print stringsRearrangement(["abc", "abx", "axx", "abc"])
