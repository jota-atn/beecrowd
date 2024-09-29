#1042 - Sorts Simples

lista = []

nums = input().split()

for i in range(3):
    num1= int(nums[i])
    lista.append(num1)

lista_2 = lista.copy()

lista.sort()

for i in range(3):
    print(lista[i])
    
print()

for i in range(3):
    print(lista_2[i])