# https://www.hackerrank.com/challenges/divisible-sum-pairs/

def divisibleSumPairs(n, k, ar):
    sum = 0
    y = 1
    for x in range(n):
        for y in range(y, n):
            if (ar[x] + ar[y]) % k == 0:
                sum += 1
        y = x+2
    return sum