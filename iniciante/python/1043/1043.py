#1043 - Triângulo

entrada = input().split()

a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])

perimetro = a + b + c
area = (a + b) * c / 2

teste_1 = a < (b + c) and a > (b - c)
teste_2 = b < (a + c) and b > (a - c) 
teste_3 = c < (b + a) and c > (b - a)


if teste_1 and teste_2 and teste_3:
    print(f"Perimetro = {perimetro:.1f}")

else:
    print(f"Area = {area:.1f}")