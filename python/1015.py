#1015 - Distância Entre Dois Pontos

x_axis = input().split()
y_axis = input().split()

x1 = float(x_axis[0])
x2 = float(y_axis[0])

y1 = float(x_axis[1])
y2 = float(y_axis[1])

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(f"{distance:.4f}")