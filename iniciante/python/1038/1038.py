#1038 - Lanche

order = input().split()

tipo = int(order[0])
number = int(order[1])

match tipo:
    case 1:
        price = 4.00
        total = price * number
        print(f"Total: R$ {total:.2f}")
    case 2:
        price = 4.50
        total = price * number
        print(f"Total: R$ {total:.2f}")
    case 3:
        price = 5.00
        total = price * number
        print(f"Total: R$ {total:.2f}")
    case 4:
        price = 2.00
        total = price * number
        print(f"Total: R$ {total:.2f}")
    case 5:
        price = 1.50
        total = price * number
        print(f"Total: R$ {total:.2f}")