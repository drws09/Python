# Comecei a estudar Python, esse pequeno script mostra os 30 primeiros números da sequencia Fibonacci:

num1 = 0
num2 = 1
fibonacci = "1"

for x in range(29):
    num3 = num1 + num2
    fibonacci += ', ' + str(num3)
    num1 = num2
    num2 = num3

print(fibonacci)

"""
Estou gostando muito de Python! 
Como diz o trecho daquela música "Codar" da banda Pypas da Língua:
Quero lhe falar
É bom programar
Codar pelo mundo a fora
C# é muito bom
Python é demais
; é algo que não vou esquecer jamais
"""