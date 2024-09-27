#1040 - Média 3

grades = input().split()

n1 = float(grades[0])
n2 = float(grades[1])
n3 = float(grades[2])
n4 = float(grades[3])

peso_n1 = 2
peso_n2 = 3
peso_n3 = 4
peso_n4 = 1

soma_pesos = peso_n1 + peso_n2 + peso_n3 + peso_n4

media = (n1 * peso_n1 + n2 * peso_n2 + n3 * peso_n3 + n4 * peso_n4) / soma_pesos

print(f"Media: {media:.1f}")

if media >= 7:
    print("Aluno aprovado.")
    
elif media < 5:
    print("Aluno reprovado.")

elif media >= 5 and media <= 6.9:
    print("Aluno em exame.")
    exam = float(input())
    print(f"Nota do exame: {exam:.1f}")
    media = (media + exam) / 2
    
    if media > 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media:.1f}")