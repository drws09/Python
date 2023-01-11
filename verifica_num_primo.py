# Praticando Pyhton: este é um código simples que verifica se um número é primo ou não

def is_prime(n):
    multiplos = 0
    for i in range(1, n+1):
        if n % i == 0:
            multiplos += 1
    if multiplos == 2:
        print(str(n) + ' É Primo')
    else:
        print(str(n) + ' Não é Primo')

for x in range(1, 101):
    is_prime(x)