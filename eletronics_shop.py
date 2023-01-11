# https://www.hackerrank.com/challenges/electronics-shop/

def getMoneySpent(keyboards, drives, b):
    options = []

    if len(keyboards) >= len(drives):
        for x in keyboards:
            for y in drives:
                if x + y <= b:
                    options.append(x+y)
    else:
        for x in drives:
            for y in keyboards:
                if x + y <= b:
                    options.append(x+y)

    if len(options) == 0:
        return -1
    else:
        options.sort()
        options.reverse()
        return options[0]