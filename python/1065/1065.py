#1065 - Pares entre Cinco Números

contador = 0
for i in range(5):  
    num = int(input())
    if num % 2 == 0:
        contador += 1
        
print(f"{contador} valores pares")