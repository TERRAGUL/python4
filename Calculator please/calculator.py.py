# -*- coding: cp1251 -*-
import math

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        return "Ошибка! Низяяя делить на 0"
    else:
        return a/b

def power(a,b):
    return a**b

def sqrt(a):
    if a < 0:
        return "Ошибка! Корень из отрицательного числа не извлекается"
    else:
        return math.sqrt(a)

def factorial(a):
    if a < 0:
        return "Ошибка! Нельзя вычислить факториал отрицательного числа"
    else:
        return math.factorial(a)

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def tan(a):
    return math.tan(a)

def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print ("Ошибка! Введите циферку((")

def get_operation(prompt):
    valid_operations = ['+','-','*','/','**','sqrt','!','sin','cos','tan']
    while True:
        operation = input(prompt)
        if operation in valid_operations:
            return operation
        else:
            print ('Ошибка! Неверная операция')

def calculator():
    a = get_number('Введите первую циферку ;): ')
    operation = get_operation('Введите одну из этих штучек: (+, -, *, /, **, sqrt, !, sin, cos, tan:) ')


    if operation in ['sqrt','!','sin','cos','tan']:
        result = None
        if operation == 'sqrt':
            result = sqrt(a)
        elif operation == '!':
            result = factorial(a)
        elif operation == 'sin':
            result = sin(a)
        elif operation == 'cos':
            result = cos(a)
        elif operation == 'tan':
            result = tan(a)

        print ('Результатион: ', result)
    else:
        b = get_number ('Ну теперь можно и вторую циферку): ')
        result = None
        if operation == '+':
            result = add(a,b)
        elif operation == '-':
            result = subtract(a,b)
        elif operation == '*':
            result = multiply(a,b)
        elif operation == '/':
            result = divide(a,b)
        elif operation == "**":
            result = power(a,b)

        print ('Ответтт: ', result)

calculator()

