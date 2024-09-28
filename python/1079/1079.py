#1079 - Médias Ponderadas

n = int(input())

for i in range(n):
    entrada = [float(e) for e in input().split()]
    a = entrada[0] * 2
    b = entrada[1] * 3
    c = entrada[2] * 5
    media = (a + b + c)/(2+3+5)
    print(f"{media:.1f}")