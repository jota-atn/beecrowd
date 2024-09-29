#1021 - Notas e Moedas

money = float(input())

notas = [100, 50, 20, 10, 5, 2]
coins = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

lista = []
lista_coins = []

for i in range(len(notas)):
    change = money // notas[i]
    lista.append(change)
    money = money % notas[i]

    
for i in range(len(coins)):
    change_coins = money / coins[i]
    lista_coins.append(change_coins)
    money = round(money % coins[i], 2)
    
    
print("NOTAS:")
for i in range(len(notas)):
        print("%d nota(s) de R$ %.2lf" %(lista[i], notas[i]))

print("MOEDAS:")
for i in range(len(coins)):
    print("%d moeda(s) de R$ %.2lf" %(lista_coins[i], coins[i]))