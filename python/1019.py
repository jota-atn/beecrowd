#1019 - Conversão de Tempo

time = int(input())

hora = (time // 60) // 60
minutos = (time // 60) % 60
segundos = time % 60

print(f"{hora}:{minutos}:{segundos}")