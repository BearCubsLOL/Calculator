def again():

        another = (input("Would you like to do another equation? Y/N: "))

        if another == "Y":
            calculator()
        if another == "N":
            print("Thanks!")
def num1():
    try:
        return int(input("Enter 1st Number: "))
    except:
        print("Invalid number")
        calculator()
def sign():
    sign1 = (input("Enter an operation: "))

    if sign1 == "+":
            ""

    elif sign1 == "-":
            ""

    elif sign1 == "*":
            ""

    elif sign1 == "/":
            ""
    else:
        print("Invalid operation")
        calculator()

    return sign1
def num2():
    try:
        return int(input("Enter 2nd Number: "))
    except:
        print("Invalid number")
        calculator()
def run(sign1, number1, number2):
    if sign1 == "+":
            print(number1 + number2)

    if sign1 == "-":
            print(number1 - number2)

    if sign1 == "*":
            print(number1 * number2)

    if sign1 == "/":
            print(number1 / number2)
def calculator():
    return1 = num1()
    return2 = sign()
    return3 = num2()     
    run(return2, return1, return3) 
    again()
print("Use + for addition")
print("Use - for subtraction")
print("Use * for multiplication")
print("Use / for division")
calculator()
