# https://www.hackerrank.com/challenges/plus-minus/

def plusMinus(arr):
    plus_count = minus_count = zero_count = 0

    for x in arr:
        if x > 0:
            plus_count += 1
        elif x < 0:
            minus_count += 1
        else:
            zero_count += 1

    plus_median, minus_median, zero_median = plus_count / len(arr), minus_count / len(arr), zero_count / len(arr)

    print(f'{plus_median:.6f}')
    print(f'{minus_median:.6f}')
    print(f'{zero_median:.6f}')