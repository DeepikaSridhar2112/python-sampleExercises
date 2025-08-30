import random
def statusOfGuessedNumber(guessedNumber):
    if(isNotInValidRange(guessedNumber)):
        return ("Enter a number in valid range",0)
    if(guessedNumber > luckySecretNumber):
        return ("Your guess should be less than " + str(guessedNumber),0)
    elif(guessedNumber < luckySecretNumber):
        return ("Your guess should be greater than " + str(guessedNumber),0)
    else:
      return ("You guessed the number correct",1)

def isNotInValidRange(number):
    if(number < lowerBound or number > uppperBound):
        return True
    return False
def captureInputs():
    lowerBoundInput = input("Enter lower bound: ")
    uppperBoundInput = input("Enter Upper Bound: ")
    return (int(lowerBoundInput), int(uppperBoundInput))   
def convertStringToInt(inputToConvert):
    try:
        return int(inputToConvert)
    except ValueError:
        return None
    

lowerBound, uppperBound = captureInputs()
while(lowerBound>=uppperBound):
    print("Enter valid values for lower bound and upper bound")
    lowerBound, uppperBound = captureInputs()
luckySecretNumber = random.randint(int(lowerBound), int(uppperBound))
print( luckySecretNumber )
status = 0
chanceCounter = 10
while status!=1 and chanceCounter>0:
    guessedNumberInput = input(f"Guess Your number within {chanceCounter} chances ")
    guessedNumber = convertStringToInt(guessedNumberInput)
    if(guessedNumber == None):
        print("Enter a valid number")
    else:
        result, status = statusOfGuessedNumber(guessedNumber)
        print(result)
    chanceCounter-=1
    