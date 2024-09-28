#1072 - Intervalo 2

n = int(input())

contador_in = 0
contador_out = 0
for i in range(n):
    x = int(input())
    if x >= 10 and x <= 20:
        contador_in += 1
    
    else:
        contador_out += 1
        
print(f"{contador_in} in")
print(f"{contador_out} out")