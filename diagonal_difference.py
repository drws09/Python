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
    print(diff)
    return diff

arr = [[-1, 2, 3, 4, -5], [-1, 2, -3, -4, 5], [-1, -2, 3, 4, 5], [-1, 2, 3, 4, -5], [1, -2, -3, -4, -5]]

diagonalDifference(arr)