# https://www.hackerrank.com/challenges/migratory-birds/

def migratoryBirds(arr):
    type1 = arr.count(1)
    type2 = arr.count(2)
    type3 = arr.count(3)
    type4 = arr.count(4)
    type5 = arr.count(5)

    bird_types = [type1, type2, type3, type4, type5]
    higherCount = max(bird_types)

    for x in range(5):
        if bird_types[x] == higherCount:
            return x+1
