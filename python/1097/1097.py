#1097 - Sequência IJ 3

i = 1
inicio = 7
fim = 4
while True:
    for j in range(inicio, fim, -1):
        print(f"I={i} J={j}")
    
    i += 2
    inicio += 2
    fim += 2
    
    if i > 9:
        break