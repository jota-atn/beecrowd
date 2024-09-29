#1010 - Cálculo Simples

part1 = input() + " "
part2 = input() + " "

lista = []
lista_2 = []
a = ''
b = ''

for i in range(len(part1)):
    if len(a) >= 1 and part1[i] == " ":
        lista.append(a)
        a = ''
    else:
        a += part1[i]


for i in range(len(part2)):
    if len(b) >= 1 and part2[i] == " ":
        lista_2.append(b)
        b = ''
    else:
        b += part2[i]

part1_num = int(lista[1])
part1_val = float(lista[2])

part2_num = int(lista_2[1])
part2_val = float(lista_2[2])

value = (part1_num * part1_val) + (part2_num * part2_val)

print(f"VALOR A PAGAR: R$ {value:.2f}")