#1018 - Cédulas 

cedulas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00]
lista = []

value = int(input())
print(value)

for i in range(len(cedulas)):
    money = value // cedulas[i]
    lista.append(int(money))
    resto = value % cedulas[i]
    value = resto

for i in range(len(cedulas)):
    cedulas[i] = str(cedulas[i])
    cedulas[i] = cedulas[i].replace(".", ",")
    cedulas[i] = cedulas[i] + '0'

for i in range(len(cedulas)):
    print(f"{lista[i]} nota(s) de R$ {cedulas[i]}")