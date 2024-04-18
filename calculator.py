
#sum function
def addNums():
    num1 = int(input("Please enter your first number: "))
    num2 = int(input("Please enter your second number: "))
    sum = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum}")
    return sum

#dif function
def subtractNums():
    num1 = int(input("Please enter your first number: "))
    num2 = int(input("Please enter your second number: "))
    difference = num1 - num2
    print(f"The difference between {num1} and {num2} is {difference}")
    return difference

#qou function
def divideNums():
    num1 = int(input("Please enter your first number: "))
    num2 = int(input("Please enter your second number: "))
    qoutient = num1 / num2
    print(f"The qoutient of {num1} and {num2} is {qoutient}")
    return qoutient

#pro function
def multiplyNums():
    num1 = int(input("Please enter your first number: "))
    num2 = int(input("Please enter your second number: "))
    product = num1 * num2
    print(f"The product of {num1} and {num2} is {product}")
    return product

#exponent num
def expoNums():
    num1 = int(input("Please enter your first number: "))
    num2 = int(input("Please enter your second number: "))
    exponential = num1 ** num2
    print(f"The exponential of {num1} and {num2} is {exponential}")
    return exponential

#squareroot of a num
def squareNums():
    num = int(input("Please enter your number: "))
    squareRoot = num ** 0.5
    print(f"The square root of {num} is {squareRoot}")
    return squareRoot

#factorial of a num
def factorialNum():
    num = int(input("Please enter your number: "))
    factorial = factorial(num)
    print(f"The factorial of {num} is {factorial}")
    return factorial




    


def main():
    # addNums()
    # subtractNums()
    # multiplyNums()
    # divideNums()
    # expoNums()
    squareNums()
    # factorialNum()

main()