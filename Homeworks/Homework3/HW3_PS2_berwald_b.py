# Homework 3
# Program Set 2
# Student Name: Bryce Berwald
# Student ID#: 1212962
# Program Description: This program will determine whether or not a credit card is valid using a
# few different logic rules and a couple different functions to handle certain tasks. The numbers 
# will be added and multiplied by two for the even positions and the odd positions will only be 
# added. The total of these sums will use modular arithmetic to determine if the card is valid or not.

def isValid(number : str)->bool:
    '''Function checks whether the credit card is valid or not'''

    placementTotal = sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)
    remainder = placementTotal % 10
    if(remainder == 0):
        return True
    else:
        return False


def sumOfDoubleEvenPlace(cardNumber : str)->int: 
    '''Function finds a single digit from the double of even indexes'''

    # Find the length of the credit card.
    cardLength = len(cardNumber)

    # Initialize sum to zero.
    doubleEvenSum = 0

    # Loop through the even placement of the credit card number.
    for i in range(0, cardLength, 2):
        # Call function to determine its double as single digit number.
        single_digit = getDigit(cardNumber[i])
        # Sum the single digit number.
        doubleEvenSum += single_digit
    
    return doubleEvenSum


def getDigit(number : str)->int:
    '''Function calculates and returns a single digit integer'''

    # Convert to integer and double the number.
    digit = int(number) * 2

    if (digit < 10):
        return digit
    else:
        strDigit = str(digit)
        return int(strDigit[0]) + int(strDigit[1])


def sumOfOddPlace(cardNumber : str)->int:
    '''Function sums the odd indexes to be returned'''
    
    # Find the length of the credit card number.
    cardLength = len(cardNumber)
    
    # Initialize the sum to zero.
    sum = 0

    # Loop through odd placements of the credit card number.
    for i in range(1, cardLength, 2):
        sum += int(cardNumber[i])
    
    return sum
        

def main():

    # Ask the user how many credit card validity cchecks they would like to perform.
    numberOfChecks = int(input("How many credit card numbers do you want to check? "))

    # Loop the number of times specified by the user.
    for i in range(0, numberOfChecks, 1):

        # user will input the credit card number as a string
        creditCardNumber = str(input("Enter a credit card number: "))

        #call the function isValid() and print whether the credit card number is valid or not valid
        if(isValid(creditCardNumber)):
            print(creditCardNumber, "is valid.")
        else:
            print(creditCardNumber, "is invalid.")
        print("")


if __name__ == "__main__":
    main()

## Test run #1 for Homework #3/Program Set #2
## How many credit card numbers do you want to check? 2
## Enter a credit card number: 4388576018402626
## 4388576018402626 is invalid.
##
## Enter a credit card number: 4388576018410707
## 4388576018410707 is valid.
##
## >>> 
##
##
## Test run #2 for Homework #3/Program Set #2
## How many credit card numbers do you want to check? 0
## >>> 
##
##
## Test run #3 for Homework #3/Program Set #2
## How many credit card numbers do you want to check? 3
## Enter a credit card number: 12345678
## 12345678 is invalid.
##
## Enter a credit card number: 5169769005222217
## 5169769005222217 is valid.
##
## Enter a credit card number: 6011655276746808
## 6011655276746808 is invalid.
##
## >>> 
##
##
## Test run #4 for Homework #3/Program Set #2
## How many credit card numbers do you want to check? 10
## Enter a credit card number: 5088900077654321
## 5088900077654321 is invalid.
##
## Enter a credit card number: 3780780098766540
## 3780780098766540 is invalid.
##
## Enter a credit card number: 6700454567889090
## 6700454567889090 is invalid.
##
## Enter a credit card number: 6565700087654681
## 6565700087654681 is invalid.
##
## Enter a credit card number: 3789876590457656
## 3789876590457656 is invalid.
##
## Enter a credit card number: 5455908870994545
## 5455908870994545 is invalid.
##
## Enter a credit card number: 5050676788909000
## 5050676788909000 is invalid.
##
## Enter a credit card number: 3765800098787656
## 3765800098787656 is invalid.
##
## Enter a credit card number: 5000000000000000
## 5000000000000000 is invalid.
##
## Enter a credit card number: 3700000000000000
## 3700000000000000 is invalid.
##
## >>> 
##
##
## Test run #5 for Homework #3/Program Set #2
## How many credit card numbers do you want to check? 10
## Enter a credit card number: 4545789098786000
## 4545789098786000 is invalid.
##
## Enter a credit card number: 5050676788991000
## 5050676788991000 is invalid.
##
## Enter a credit card number: 3737800090908776
## 3737800090908776 is invalid.
##
## Enter a credit card number: 3765898909989880
## 3765898909989880 is invalid.
##
## Enter a credit card number: 5000600050005577
## 5000600050005577 is invalid.
##
## Enter a credit card number: 4388576018402626
## 4388576018402626 is invalid.
##
## Enter a credit card number: 5169769005222217
## 5169769005222217 is valid.
##
## Enter a credit card number: 6000500068901010
## 6000500068901010 is invalid.
##
## Enter a credit card number: 5800776590806545
## 5800776590806545 is invalid.
##
## Enter a credit card number: 4040708890907888
## 4040708890907888 is invalid.
##
## >>> 