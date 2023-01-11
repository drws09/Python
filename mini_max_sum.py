# https://www.hackerrank.com/challenges/mini-max-sum/

def miniMaxSum(arr):
    mins = arr.copy()
    mins.sort()
    maxs = mins.copy()
    maxs.reverse()
    min_sum = max_sum = 0

    for x in range(4):
        min_sum += mins[x]
        max_sum += maxs[x]
    
    print(min_sum, max_sum)