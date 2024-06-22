
import math
from error_handling import *

def addNums(num1, num2):
    sum = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum}")
    return sum


def subtractNums(num1, num2):
    difference = num1 - num2
    print(f"The difference between {num1} and {num2} is {difference}")
    return difference


def divideNums(num1, num2):
    try:
        qoutient = num1 / num2
        print(f"The qoutient of {num1} and {num2} is {qoutient}")
    except ZeroDivisionError:
        zero_num_operation()    
    return qoutient


def multiplyNums(num1, num2):
    product = num1 * num2
    print(f"The product of {num1} and {num2} is {product}")
    return product


def expoNums(num1, num2):
    exponential = num1 ** num2
    print(f"{num1} to the power of {num2} is {exponential}")
    return exponential


def squareNums(num1):
    try:
        squareRoot = round(num1 ** 0.5, 2)
        print(f"The square root of {num1} is {squareRoot}")
        return squareRoot
    except ValueError:
        zero_num_operation()
        


def factorialNum(num1):
    try:
        factorial = math.factorial(num1)
        print(f"The factorial of {num1} is {factorial}")
        return factorial
    except ValueError:
        zero_num_operation()




