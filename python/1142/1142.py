#1142 - PUM

n = int(input())

contador = 0
for i in range(n):
    string = ""
    for j in range(4):
        contador += 1
        if j == 3:
            string += "PUM"
            break
        string += f"{contador} "
    
    print(string)