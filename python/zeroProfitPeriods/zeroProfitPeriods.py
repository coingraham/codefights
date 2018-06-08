"""
Lindsey, a small fox, has a bank account. She has a list of her transactions during some period of time. Negative transactions[i] means that the money leaves the account, and positive transactions[i] means that money is added to the account.

Lindsey refers to the sum of consecutive transactions as the profit of these transactions. She wants to find the maximum number of non-overlapping periods of consecutive transactions with zero profit. Please, help the fox.

Example

For transactions = [1, 1, 2, -3, 0, 1000, 6, -6, 1, 1, 1, -3, 2], the output should be
zeroProfitPeriods(transactions) = 4.

The periods [1, 2, -3], [0], [6, -6], [1, 1, 1, -3] are each zero-profit. Also, the periods [1, 2, -3], [0], [6, -6], [1, -3, 2] are zero-profit as well.

Input/Output

[execution time limit] 4 seconds (py)

[input] array.integer transactions

A list of Lindsey's bank transactions, in chronological order. Positive values represent deposits, and negative values represent withdrawals.

Guaranteed constraints:
1 <= transactions.length <= 105,
-103 <= transactions[i] <= 103.

[output] integer

The maximum number of non-overlapping periods of consecutive transactions with zero profit.
"""

# hat tip to user jay_d14
def zeroProfitPeriods(transactions):

    running_total = 0

    for entry in transactions:
        running_total += entry

        if running_total != 0:
            print running_total
        else:
            print "Zero Profit"


# One of the solutions by user jay_d14
def zeroProfitPeriods_solutions(transactions):

    # We're going to keep a running sum as we go
    running_sum = 0

    # We'll collect a total of 0 profit sets
    total = 0

    # We get a set of running sums
    set_of_running_sums = {0}

    # Loop through transactions once O(n)
    for t in transactions:

        # Add the transaction to the running sum
        running_sum += t

        # If the running sum is in the set, up the count of zero profits and reset
        if running_sum in set_of_running_sums:
            total += 1
            set_of_running_sums = {0}
            running_sum = 0

        # Add the current running sum to the set
        set_of_running_sums.add(running_sum)

    # Return the total sums you've counted
    return total


if __name__ == '__main__':

    # print zeroProfitPeriods_solutions([1, 1, 2, -3, 0, 1000, 6, -6, 1, 1, 1, -3, 2])
    print zeroProfitPeriods_solutions([1, 1, -2, -2, -2, 1, 1, 1, -2, 1, -2, 1, 1, 1, -2,
                             1, 1, 1, 1, 1, 1, -2, -2, 1, 1, 1, -2, 1, 1, -2])
