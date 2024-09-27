#1020 - Idade em Dias

idade = int(input())
datas = ["ano(s)", "mes(es)", "dia(s)"]
divs = [365, 30, 1]
resto = idade
lista = []

for i in range(len(datas)):
    age = resto // divs[i]
    lista.append(age)
    resto = resto % divs[i]

for i in range(len(datas)):
   print(f"{lista[i]} {datas[i]}")