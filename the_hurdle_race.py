# https://www.hackerrank.com/challenges/the-hurdle-race/

def hurdleRace(k, height):
    height.sort()
    height.reverse()
    potions = 0

    while k < height[0]:
        potions += 1
        k += 1
    
    return potions