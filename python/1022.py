#1022 - TDA Racional

def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())

for i in range(n):
    entrada = input().split()
    n1 = int(entrada[0])
    d1 = int(entrada[2])
    sinal = entrada[3]
    n2 = int(entrada[4])
    d2 = int(entrada[6])
    
    if sinal == "+":
        numerador = (n1*d2 + n2*d1)
        denominador =(d1*d2)
        
    elif sinal == "-":
        numerador = (n1*d2 - n2*d1)
        denominador =(d1*d2)
        
    elif sinal == "*":
        numerador = (n1*n2)
        denominador =(d1*d2)
        
    else:
        numerador = (n1*d2)
        denominador =(n2*d1)
    
    msg = f"{numerador}/{denominador} = {numerador//mdc(numerador, denominador)}/{denominador//mdc(numerador, denominador)}"
    print(msg)