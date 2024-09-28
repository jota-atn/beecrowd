#1046 - Tempo de Jogo

lista_horas = []

for i in range(24):
    lista_horas.append(i)
    
entrada = input().split()
hora_inicial = int(entrada[0])
hora_final = int(entrada[1])

indice = hora_inicial
contador = 0
while True:
    if indice == len(lista_horas):
        indice = 0
        
    if indice == hora_final and contador != 0:
        break
    
    indice += 1
    contador += 1
    
print(f"O JOGO DUROU {contador} HORA(S)")