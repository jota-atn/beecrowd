#1017 - Gasto de Combustível

time = int(input())
velocity = int(input())

distance = velocity * time
consume = distance / 12

print(f"{consume:.3f}")