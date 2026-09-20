# задача №1

##n = int(input("Сколько человек? "))
##
##summa = 0
##
##for i in range(n):
##    vozrast = int(input("Введите возраст: "))
##    summa = summa + vozrast
##
##sredniy = summa / n
##print("Средний возраст:", sredniy)

# задача №2

code = input("Введите код цвета (например a0351f): ")

if code == "000000":
    print("черный")
elif code == "ffffff":
    print("белый")
else:

    r = int(code[0:2], 16)
    g = int(code[2:4], 16)
    b = int(code[4:6], 16)

    if r == g and g == b:
        print("серый")
    elif r > g and r > b:
        print("ближе к красному")
    elif g > r and g > b:
        print("ближе к зеленому")
    elif b > r and b > g:
        print("ближе к синему")
