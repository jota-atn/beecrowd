#1041 - Coordenadas de um Ponto

coords = input().split()

x = float(coords[0])
y = float(coords[1])

if (x > 0 or x < 0) and (y > 0 or y < 0):
    if x > 0 and y > 0:
        print("Q1")
    elif x < 0 and y > 0:
        print("Q2")
    elif x < 0 and y < 0:
        print("Q3")
    else:
        print("Q4")
    
else:
    if x == 0 and y != 0:
        print("Eixo Y")
    elif x != 0 and y == 0:
        print("Eixo X")
    else:
        print("Origem")