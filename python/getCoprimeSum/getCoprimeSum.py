"""
Given an integer n, we'd like to find the sum of all integers between 1 and n (inclusive) that are relatively prime to n.

Since this number can be quite large, return the sum mod 109 + 7.

Example

For n = 10 the output should be getCoprimeSum(n) = 20.

d	1	2	3	4	5	6	7	8	9	10
gcd(n, d)	1	2	1	2	5	2	1	2	1	10
Only 1, 3, 7, and 9 are relatively prime with n, and 1 + 3 + 7 + 9 = 20.

Input / Output

[execution time limit] 4 seconds (py)

[input] integer n

A non-negative integer that we're trying to find coprimes with respect to.

Guaranteed constraints:
1 <= n <= 108

[output] integer

The sum of all numbers less than or equal to n that are relatively prime to n (mod 109 + 7)
"""

# This is a solution but it isn't fast enough  it's O(n^2)
def getCoprimeSum_slow(n):

    coprime_list = []

    exclusion_list = []

    for number in range(2, n + 1):
        modulo = n % number

        if modulo == 0:
            exclusion_list.append(number)
        else:
            also_exclude = False
            for excluded in exclusion_list:
                if number % excluded == 0:
                    also_exclude = True

            if also_exclude:
                exclusion_list.append(number)
            else:
                coprime_list.append(number)

    return sum(coprime_list) + 1


# Attempting to use recursion and that's way too slow.
# def do_euclidean_algo(a, b):
#
#     remainder = a % b
#
#     if remainder == 0:
#         return b
#     else:
#         return do_euclidean_algo(b, remainder)

def getCoprimeSum_faster_but_not_good_enough(n):

    # master_list = [x for x in range(2, n + 1)]

    coprime_sum = 1
    offset = 0

    if n % 2 == 0:
        offset = 2

    if n % 3 == 0:
        offset = 3

    if n % 5 == 0:
        offset = 5

    if n % 7 == 0:
        offset = 7

    for number in list_generator(n, offset):
        for gcd, remainder in do_euclidean_generator(n, number):
            pass

        if gcd == 1:
            # print number
            coprime_sum += number

    return coprime_sum % (10**9 + 7)


def list_generator(n, offset):

    if offset == 0:
        for x in range(2, n + 1):
            yield x
    else:
        for x in range(2, n + 1):
            if x % offset != 0:
                yield x


def do_euclidean_generator(a, b):

    remainder = 1

    while remainder != 0:
        remainder = a % b
        a = b
        b = remainder
        yield a, b


def getCoprimeSum(number):

    prime_factor_list = []

    is_odd = number % 2

    i = 2
    n = number

    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            prime_factor_list.append(i)

    if n > 1:
        prime_factor_list.append(n)

    coprime_sum = float((number ** 2) / 2)

    for factor in set(prime_factor_list):
        multiplier = (1 - (1 / float(factor)))
        coprime_sum *= multiplier

    if is_odd:
        return int(coprime_sum + 1) % (10 ** 9 + 7)
    else:
        return int(coprime_sum) % (10 ** 9 + 7)


if __name__ == '__main__':
    print getCoprimeSum(105)

    print getCoprimeSum_faster_but_not_good_enough(105)

