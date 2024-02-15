def again():

        another = (input("Would you like to do another equation? Y/N: "))
        if another.upper() == "Y":
            calculator()
        elif another.upper() == "N":
            print("Thanks!")
        else:
            print("Invalid try again")
            again()
def num1():
    return float(input("Enter 1st Number: "))
def sign():
    sign1 = (input("Enter an operation: "))

    if sign1 == "+":
            pass

    elif sign1 == "-":
            pass

    elif sign1 == "*":
            pass

    elif sign1 == "/":
            pass
            
    elif sign1.upper() == "R":
            pass
        
    elif sign1 == "^":
            pass
            
    else:
        print("10" + 3)
    
    return sign1
def num2():
    return float(input("Enter 2nd Number: "))
def run(sign1, number1, number2):
    if sign1 == "+":
        print(number1 + number2)

    if sign1 == "-":
        print(number1 - number2)

    if sign1 == "*":
        print(number1 * number2)

    if sign1 == "/":
        print(number1 / number2)
    if sign1.upper() == "R":
        print(number1 ** (1/number2))
    if sign1 == "^":
        print(number1 ** (number2))
            
def calculator():
    try:
        return1 = num1()
        return2 = sign()
        return3 = num2()
        run(return2, return1, return3) 
        again()
    except:
        print("\nInvalid try again\n")
        calculator()
print("Use + for addition\n")
print("Use - for subtraction\n")
print("Use * for multiplication\n")
print("Use / for division\n")
print("Use R for finding the root")
print("First number = the number you are finding the root of!")
print("Second number = number which you want the root to be\n")
print("Use ^ for exponentiation\n")
calculator()