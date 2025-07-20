dia1 = input().split()
dia1 = int(dia1[1]) * 86400
horario_dia1 = input().split(" : ")

dia2 = input().split()
dia2 = int(dia2[1]) * 86400
horario_dia2 = input().split(" : ")

conversoes = [3600, 60, 1]
for i in range(3):
    dia1 += int(horario_dia1[i]) * conversoes[i]
    dia2 += int(horario_dia2[i]) * conversoes[i]

total_segundos = abs(dia1 - dia2)
conversoes = [86400, 3600, 60, 1]
out = ["dia", "hora", "minuto", "segundo"]
for i in range(4):
    print(f"{total_segundos // conversoes[i]} {out[i]}(s)")
    total_segundos = total_segundos % conversoes[i]
