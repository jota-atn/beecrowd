#1080 - Maior e Posição

lista = []
for i in range(100):
    lista.append(int(input()))

maior = lista[0]
for i in range(len(lista)):
    if maior < lista[i]:
        maior = lista[i]
        indice = i + 1
        
print(maior)
print(indice)