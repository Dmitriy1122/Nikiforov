do = input("ввести арифметический оператор: ")
if do == "+":
    number1 = float(input("ввести 1 значение: "))
    number2 = float(input("ввести 2 значение: "))
    print(number1 + number2)
elif do == "-":
    number1 = float(input("ввести 1 значение: "))
    number2 = float(input("ввести 2 значение: "))
    print(number1 - number2)
elif do == "/":
    number1 = float(input("ввести 1 значение: "))
    number2 = float(input("ввести 2 значение: "))
    print(number1 / number2)
elif do == "*":
    number1 = float(input("ввести 1 значение: "))
    number2 = float(input("ввести 2 значение: "))
    print(number1 * number2)
elif do == "pow":
    number1 = float(input("ввести 1 значение: "))
    number2 = float(input("ввести 2 значение: "))
    print(pow(number1, number2))
elif do == "module":
    number1 = float(input("ввести значение: "))
    print(abs(number1))
elif do == "0":  #операция рандомное число, если нажать на ноль
    print(random.randint(0, 1000))
elif do == "div":
    number1 = float(input("ввести 1 значение: "))
    number2 = float(input("ввести 2 значение: "))
    print(number1//number2)
elif do == "mod":
    number1 = float(input("ввести 1 значение: "))
    number2 = float(input("ввести 2 значение: "))
    print(number1 % number2)
elif do == "f":
    number1 = int(input("ввести  значение: "))
    print(math.factorial(number1))
elif do == "arccos":
    number1 = float(input("ввести значение: "))
    number11 = number1*math.pi/180
    print(math.acos(number11))