def again():

        another = (input("Would you like to do another equation? Y/N: "))
        if another == "Y":
            calculator()
        elif another == "N":
            print("Thanks!")
        else:
            print("Invalid try again")
            again()
def num1():
    return int(input("Enter 1st Number: "))
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
    return int(input("Enter 2nd Number: "))
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
    try:
        return1 = num1()
        return2 = sign()
        return3 = num2()
        run(return2, return1, return3) 
        again()
    except:
        print("Invalid try again\n")
        calculator()
print("Use + for addition")
print("Use - for subtraction")
print("Use * for multiplication")
print("Use / for division")
calculator()