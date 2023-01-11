# https://www.hackerrank.com/challenges/bon-appetit/

def bonAppetit(bill, k, b):
    bill.remove(bill[k])
    sum = 0

    for x in bill:
        sum += x
        
    splitted_bill = int(sum/2)

    if splitted_bill == b:
        print('Bon Appetit')
    else:
        overcharge = b - splitted_bill
        print(overcharge)