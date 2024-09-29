#1044 - Múltiplos

nums = input().split()

num1 = int(nums[0])
num2 = int(nums[1])

if num2 > num1:
    if num2 % num1 == 0:
        msg = "Sao Multiplos"
    else:
        msg = "Nao sao Multiplos"
        
else:
    if num1 % num2 == 0:
        msg = "Sao Multiplos"
    else:
        msg = "Nao sao Multiplos"

print(msg)