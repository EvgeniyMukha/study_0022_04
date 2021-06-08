from math_two import manipulation

run = True
print(
    "/ - деление \n* - умножение \n+ - сложение \n- - разность\nm - модуль\narccos - arccos \n^ - возведение в степень \n! - факториал \nrand - рандомное число \nquit - выход")

while (run):
    command = input()

    if command == "/":
        manipulation.division(self=(''))

    elif command == "quit":
        run = False

    elif command == "*":
        manipulation.multiplication(self=(''))

    elif command == "-":
        manipulation.subtraction(self=(''))

    elif command == "+":
        manipulation.sum(self=(''))

    elif command == "^":
        manipulation.power(self=(''))

    elif command == "m":
        manipulation.mod(self=(''))

    elif command == "arccos":
        manipulation.acos(self=(''))

    elif command == "!":
        print("number =")
        number = float(input())
        print(manipulation.factorial(number))

    elif command == "rand":
        manipulation.rand(self=(''))

    else:
        print("Команда отсутствует")
