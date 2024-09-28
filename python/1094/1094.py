#1094 - Experiências

n = int(input())

cobaias = 0
coelhos = 0
ratos = 0
sapos = 0

for i in range(n):
    teste = input().split()
    cobaias += int(teste[0])
    
    if teste[1] == "C":
        coelhos += int(teste[0])
        
    elif teste[1]  == "R":
        ratos += int(teste[0])
        
    else:
        sapos += int(teste[0])
        
coelhos_porcento = (coelhos * 100) / cobaias
ratos_porcento = (ratos * 100) / cobaias
sapos_porcento = (sapos * 100) / cobaias
        
print(f"Total: {cobaias} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {coelhos_porcento:.2f} %")
print(f"Percentual de ratos: {ratos_porcento:.2f} %")
print(f"Percentual de sapos: {sapos_porcento:.2f} %")