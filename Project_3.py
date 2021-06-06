import math
import random

def factorial(number): # функция факториала
    if number == 0:
        return 1.0
    return number*factorial(number-1)

point = True
print("/ деление \n* умножение \n+ сложение \n- разность\nm модуль\narccos - arccos \n^  возведение в степень \n! факториал \nrand рандомное число \nquit выход")

while(point):
    str = input()

    if str == "/":
        print("number =")
        number = float(input())  # float - вещественные числа
        print("second number = ")
        secondnumber = float(input())
        print(number / secondnumber)

    elif str == "quit":
        point = False

    elif str == "*":
        print("number =")
        number = float(input())
        print("second number = ")
        secondnumber = float(input())
        print(number * secondnumber)

    elif str == "-":
        print("number =")
        number = float(input())
        print("second number = ")
        secondnumber = float(input())
        print(number - secondnumber)

    elif str == "+":
        print("number =")
        number = float(input())
        print("second number = ")
        secondnumber = float(input())
        print(number + secondnumber)

    elif str == "^":
        print("number =")
        number = float(input())
        print("second number = ")
        secondnumber = float(input())
        print(number ** secondnumber)

    elif str == "m":
        print("number =")
        number = float(input())
        print(math.fabs(number))

    elif str == "arccos":
        print("number =")
        number = float(input())
        print(math.acos(number))

    elif str == "!":
        print("number =")
        number = float(input())
        print(factorial(number))

    elif str == "rand":
        print("Рандомное число в диапазона от: ")
        number = int(input())
        print("До :")
        secondnumber = int(input())
        print(random.randint(number, secondnumber))

    else:
        print("Команда отсутствует")