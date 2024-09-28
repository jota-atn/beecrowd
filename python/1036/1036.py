#1036 - Fórmula de Bhaskara

entrada = input().split()

a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])

delta = b ** 2 - 4 * a * c

if delta < 0 or a == 0:
    print("Impossivel calcular")


else:
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")
