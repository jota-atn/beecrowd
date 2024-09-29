#1009 - Salário com Bônus

nome = input()
salary_fix = float(input())
sales = float(input())
comission = (15/100) * sales
salary_final = salary_fix + comission

print(f"TOTAL = R$ {salary_final:.2f}")
