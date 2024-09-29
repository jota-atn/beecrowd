#1050 - DDD

ddd = int(input())

locais = ["Brasilia", "Salvador", "Sao Paulo", "Rio de Janeiro", "Juiz de Fora", "Campinas", "Vitoria", "Belo Horizonte"]

if ddd == 61:
    print(locais[0])

elif ddd == 71:
    print(locais[1])
    
elif ddd == 11:
    print(locais[2])
    
elif ddd == 21:
    print(locais[3])
    
elif ddd == 32:
    print(locais[4])
    
elif ddd == 19:
    print(locais[5])
    
elif ddd == 27:
    print(locais[6])
    
elif ddd == 31:
    print(locais[7])
    
else:
    print("DDD nao cadastrado")