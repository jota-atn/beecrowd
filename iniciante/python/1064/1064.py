#1064 - Positivos e Média 

lista = []

contador = 0
for i in range(6):
    a = float(input())
    if a > 0:
        contador += 1
        lista.append(a)
    
media = sum(lista)/len(lista)

print(f"{contador} valores positivos")
print(f"{media:.1f}")