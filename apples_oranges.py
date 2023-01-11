# https://www.hackerrank.com/challenges/apple-and-orange/

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_roof = 0
    oranges_roof = 0

    for x in apples:
        if x + a >= s and  x + a <= t:
            apples_roof += 1
    for x in oranges:
        if x + b >= s and  x + b <= t:
            oranges_roof += 1

    print(apples_roof)
    print(oranges_roof)