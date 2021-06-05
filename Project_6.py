import math
import random

def plus(number,second_number):
    print("number =")
    number = float(input())
    print("second_number = ")
    second_number = float(input())
    return print(number + second_number)
def minus(number,second_number):
    print("number =")
    number = float(input())
    print("second number = ")
    secondnumber = float(input())
    return print(number - secondnumber)
def deleniye(number,second_number):
    print("number =")
    number = float(input())
    print("second number = ")
    secondnumber = float(input())
    return print(number / secondnumber)
def umnojeniye(number,second_number):
    print("number =")
    number = float(input())
    print("second number = ")
    secondnumber = float(input())
    return print(number * secondnumber)
def stepen(number,second_number):
    print("number =")
    number = float(input())
    print("second number = ")
    secondnumber = float(input())
    return print(number ** secondnumber)
def module(number):
    print("number =")
    number = float(input())
    return print(math.fabs(number))
def arccos(number):
    print("number =")
    number = float(input())
    return print(math.acos(number))
def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)
def random(number,second_number):
    print("Рандомное число в диапазона от: ")
    number = int(input())
    print("До :")
    secondnumber = int(input())
    return print(random.randint(number, secondnumber))

point = True
print("/ деление \n* умножение \n+ сложение \n- разность\nm модуль\narccos - arccos \n^  возведение в степень \n! факториал \nrand рандомное число \nquit выход")

while(point):
    number=0;second_number=0;str=0;
    str = input()

    if str == "/":
        deleniye(number,second_number)

    elif str == "quit":
        point = False

    elif str == "*":
        umnojeniye(number,second_number)

    elif str == "-":
        minus(number,second_number)

    elif str == "+":
        plus(number,second_number)

    elif str == "^":
        stepen(number,second_number)

    elif str == "m":
        module(number)

    elif str == "arccos":
        arccos(number)

    elif str == "!":
        print("number =")
        number = float(input())
        print(factorial(number))

    elif str == "rand":
        random(number,second_number)

    else:
        print("Команда отсутствует")