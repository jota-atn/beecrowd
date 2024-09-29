#1048 - Aumento de Salário

salario = float(input())

if salario <= 400:
    porcentagem = 15

elif salario > 400 and salario <= 800:
    porcentagem = 12
    
elif salario > 800 and salario <= 1200:
    porcentagem = 10

elif salario > 1200 and salario <= 2000:
    porcentagem = 7
    
elif salario > 2000:
    porcentagem = 4

aumento = salario * (porcentagem / 100)
novo_salario = salario + aumento

print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {aumento:.2f}")
print(f"Em percentual: {porcentagem} %")