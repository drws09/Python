# https://www.hackerrank.com/challenges/kangaroo/

def kangaroo(x1, v1, x2, v2):
    dif_x = x1 - x2
    dif_v = v1 - v2

    if x1 == x2 and v1 == v2:
        return 'YES'
    
    if x1 > x2 and v1 > v2 or x2 > x1 and v2 > v1 or x1 == x2 and v1 != v2 or v1 == v2 and x1 != x2:
        return 'NO'

    if dif_x % dif_v == 0:
        return 'YES'
    else:
        return 'NO'

""" 
Essa aqui foi a minha primeira tentativa que também teve score máximo, mas não gostei, 
ela passou em todos os testes mas não achei justo, 
então fui tentando de outras maneiras até chegar na solução de cima.

def kangaroo(x1, v1, x2, v2):
    posK1 = x1
    posK2 = x2
    
    for x in range(10000):
        posK1 += v1
        posK2 += v2
        if posK1 == posK2:
            return 'YES'
    return 'NO'
"""