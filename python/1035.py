#1035 - Teste da Seleção 1

entrada = input().split()

a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])
d = int(entrada[3])

e = (b > c)
f = (d > a)
g = (c + d) > (a + b)
h = a % 2

if e and f and g and h == 0 and c > 0 and d > 0:
    print("Valores aceitos")

else: 
    print("Valores nao aceitos")