entrada = input().split()

hora_inicial = int(entrada[0]) 
minuto_inicial = int(entrada[1])
hora_final = int(entrada[2])
minuto_final = int(entrada[3])

qtd_horas = 0
qtd_minutos = 0

if hora_inicial == hora_final and minuto_inicial == minuto_final:
    qtd_horas = 24

else:
    minuto_aux = minuto_inicial
    contador = 0
    while True:
        if hora_inicial == hora_final and minuto_inicial == minuto_final:
            qtd_minutos = (minuto_inicial - minuto_aux) % 60
            break

        minuto_inicial += 1
        contador += 1
        
        if minuto_inicial == 60:
            hora_inicial = (hora_inicial + 1) % 24
            minuto_inicial = 0

        if contador == 60:
            contador = 0
            qtd_horas += 1


print(f"O JOGO DUROU {qtd_horas} HORA(S) E {qtd_minutos} MINUTO(S)")

