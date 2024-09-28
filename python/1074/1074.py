#1074 - Par ou Ímpar

n = int(input())

for i in range(n):
    x = int(input())
    if x > 0:
        if x % 2 == 0:
            msg = "EVEN POSITIVE"
            
        else:
            msg = "ODD POSITIVE"
    elif x < 0:
        if x % 2 == 0:
            msg = "EVEN NEGATIVE"
        
        else:
            msg = "ODD NEGATIVE"
    else:
        msg = "NULL"
    
    print(msg)      