#1096 - Sequência IJ 2

i = 1
while True:
    for j in range(7, 4, -1):
        print(f"I={i} J={j}")
    i += 2
    if i > 9:
        break