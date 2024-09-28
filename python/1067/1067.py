#1067 - Números Ímpares

x = int(input())
inicio = 1

while inicio <= x:
    if inicio % 2 != 0:
        print(inicio)
    
    inicio += 2