#1051 - Imposto de Renda

valor = float(input())

if valor <= 2000:
    print("Isento")
    
else:
    lista = [1000, 1500]
    
    resto = valor - 2000
    
    indice = 0
    
    porcentagem = 0
    porcento = 8
    while True:
        if resto <= 1000:
            porcentagem += resto * (porcento/100)
            break
    
        else:
            if indice == 2:
                lista.append(resto)
                resto -= lista[indice]
                porcentagem += lista[indice] * (porcento/100)
            
            else:
                resto -= lista[indice]
                porcentagem += lista[indice] * (porcento/100)
                indice += 1
            
        porcento += 10

    print(f"R$ {porcentagem:.2f}")