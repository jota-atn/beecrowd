#1045 - Tipos de Triângulos

entrada = [float(e) for e in input().split()]
a, b, c = entrada[0], entrada[1], entrada[2]
A = round(max(a, b, c), 2)
C = round(min(a, b, c), 2)
B = round((a + b + c - A - C), 2)

if A >= B + C:
    print("NAO FORMA TRIANGULO")
    
else:
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
        
    if A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
        
    if A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")

    if (A == B and A == C):
        print("TRIANGULO EQUILATERO")
        
    elif A == B or B == C or A == C:
        print("TRIANGULO ISOSCELES")