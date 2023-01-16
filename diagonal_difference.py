# https://www.hackerrank.com/challenges/diagonal-difference/

def diagonalDifference(arr):
    sumA = 0
    sumB = 0
    fw = 0
    bw = len(arr) - 1

    for x in arr:
        sumA += x[fw]
        fw += 1
        sumB += x[bw]
        bw -= 1
        
    diff = abs(sumA - sumB)
    return diff
