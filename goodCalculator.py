#takes two numbers and returns sum
def add(addend1, addend2):
    return addend1 + addend2

#takes two numbers and returns difference
def subtract(minuend, subtrahend):
    return minuend - subtrahend

#takes two numbers and returns product
def multiply(factor1, factor2):
    return factor1 * factor2

#takes two numbers and returns quotient
def divide(dividend, divisor):
    return dividend / divisor

while True:
    #getting input for calculation
    firstNumber = int(input('Enter First Number: '))
    operator = input('Enter Operator(+, -, /, *) or anything else to quit: ')
    secondNumber = int(input('Enter Second Number: '))

    #call method to perform calculation
    if operator == '+':
        print(add(firstNumber, secondNumber))
    elif operator == '-':
        print(subtract(firstNumber, secondNumber))
    elif operator == '/':
        print(divide(firstNumber, secondNumber))
    elif operator == '*':
        print(multiply(firstNumber, secondNumber))
    else:
        print('Invalid Operator')
        exit()
