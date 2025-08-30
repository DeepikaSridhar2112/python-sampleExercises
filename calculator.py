def calculate(input1, input2, operator):
    if(isValidOperator(operator) == False):
        return "invalid operator provided"
    number1 = parseInput(input1)
    number2 = parseInput(input2)
    if(isValidInputs(number1,number2) == False):
      return "please input a valid number"
    if(operator == "+"):
        return number1 + number2;
    elif(operator == "-"):
        return number1 - number2;
    elif(operator == "*"):
        return number2 * number1 
    else:
       return number1/number2;

def isValidInputs(input1, input2):
    if(input1==None or input2==None):
        return False
    else:
        return True
def parseInput(inputString):
    try:
        integer_value = int(inputString)
        return integer_value
    except ValueError:
        return None
def isValidOperator(operator):
    allowedOperatorList = ["+","-","*","/"]
    if(operator not in (allowedOperatorList)):
        return False
    else:
        return True

def getUserInputs():
    number1 = input("enter number 1: ")
    number2 = input("enter number 2: ")
    operator = input("enter operation to be performed: ")
    return number1, number2, operator


while True:
    print("Welcome to Calculator.. Press Ctrl+C to exit.")
    try:
        number1, number2, operator = getUserInputs();
        print(f"The result : {calculate(number1, number2, operator)}")
    except KeyboardInterrupt:
         print("\nCtrl+C detected. Exiting calculator.")

