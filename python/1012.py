#1012 - Área

string = input() + " "
lista = []
a = ""

for i in range(len(string)):
    if len(string) > 1 and string[i] == " ":
        lista.append(a)
        a = ''
    else:
        a += string[i]

A = float(lista[0])
B = float(lista[1])
C = float(lista[2])

pi = 3.14159

area_triangle = (A * C) / 2
area_circle = C ** 2 * pi
area_trapeze = ((A + B) * C) / 2
area_square = B ** 2
area_rectangle = A * B

print(f"TRIANGULO: {area_triangle:.3f}")
print(f"CIRCULO: {area_circle:.3f}")
print(f"TRAPEZIO: {area_trapeze:.3f}")
print(f"QUADRADO: {area_square:.3f}")
print(f"RETANGULO: {area_rectangle:.3f}")