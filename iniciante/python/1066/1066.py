#1066 - Pares, Ímpares, Positivos e Negativos

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(5):
    num = int(input())
    
    if num == 0:
        pares += 1
    
    elif num > 0:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
        positivos += 1
    else:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
        negativos += 1
        
print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")