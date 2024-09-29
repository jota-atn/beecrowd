#1049 - Animal

estrutura = input().upper()
tipo = input().upper()
alimentacao = input().upper()

if estrutura == "VERTEBRADO":
    if tipo == "AVE":
        if alimentacao == "CARNIVORO":
            print("aguia")
        elif alimentacao == "ONIVORO":
            print("pomba")
    
    elif tipo == "MAMIFERO":
        if alimentacao == "ONIVORO":
            print("homem")
        elif alimentacao == "HERBIVORO":
            print("vaca")
    
elif estrutura == "INVERTEBRADO":
    if tipo == "INSETO":
        if alimentacao == "HEMATOFAGO":
            print("pulga")
        elif alimentacao == "HERBIVORO":
            print("lagarta")
    
    elif tipo == "ANELIDEO":
        if alimentacao == "HEMATOFAGO":
            print("sanguessuga")
        elif alimentacao == "ONIVORO":
            print("minhoca")