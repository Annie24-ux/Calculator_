from operations import addNums, divideNums, expoNums, factorialNum, multiplyNums, squareNums, subtractNums
from error_handling import *


def get_operation():
    operation = input("What operation would you like to do? ").lower().strip()    
    return operation

def is_valid_operation(operation):
    operations = ["sum", "add", "+", "*", "multiply", "divide", "/", "squareroot",
                  "root", "product", "difference", "power", "square", "exponents","minus", "-", "factorial", "!", ]
    
    if (operation in operations):
        return True
    else:
        print(f"'{operation}'is an invalid operation.")
        return False
    

def get_inputs(operation):
    single_inputs = ["factorial", "!", "square root", "square", "root"]

    while True:
        try:
            if operation in single_inputs:
                num1 = int(input("Please enter your number: "))
                return num1, None
            else:
                num1 = int(input("Please enter your first number: "))
                num2 = int(input("Please enter your second number: "))
                return num1, num2
            
        except ValueError:
            invalid_input()        
    
def get_result(operation, num1, num2 = None):    
    result = 0
    if (operation == "sum" or operation == "+"):
        result = addNums(num1, num2)
    elif (operation == "difference" or operation == "minus" or operation == "-"):    
        result = subtractNums(num1, num2)
    elif (operation == "product" or operation == "multiplication" or operation == "*"):
        result = multiplyNums(num1, num2)
    elif (operation == "divide" or operation == "qoutient" or operation == "/"):
        result = divideNums(num1, num2)    
    elif (operation == "square" or operation == "exponent" or operation == "power"):
        result = expoNums(num1, num2)
    elif (operation == "square root" or operation == "root"):
        result = squareNums(num1)
    elif (operation == "factorial" or operation == "!"):
        result = 1
        result *= factorialNum(num1)
    
    else:
        print(f"Sorry, that's {operation}an Invalid operation.") 
        help()  
        
            
             
        

def main():
    operation = get_operation()
    while (is_valid_operation(operation)):
        num1, num2 = get_inputs(operation)
        get_result(operation, num1, num2)
        break
    else:
        get_operation()
    
            
    
   

if __name__ == "__main__":
    main()