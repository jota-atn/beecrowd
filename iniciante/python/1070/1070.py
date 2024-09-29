#1070 - Seis Números Ímpares

x = int(input())

contador = 0
while True:
    if contador == 6:
        break
    
    if x % 2 != 0:
        contador += 1
        print(x)
        
    x += 1