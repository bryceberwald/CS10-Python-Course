# Homework 2
# Program Set 1
# Student Name: Bryce Berwald
# Student ID#: 1212962
# Program Description: The program will ask the user to enter a two digit number until the user enters
# -999 as the sentienal value. Each time through the loop a new 2 digit lotto number will be
# generated and used for comparsion with the number inputted. Depending on the guess, the user has 
# the chance to win a certain amount of money.

# Libraries
import random

# Variables & Constants
lotteryGuessedNumber = 0

# Processing/Calculations
while(lotteryGuessedNumber != -999):
    randomLotteryNumber = random.randint(10, 99)
    theFirstNumOfRandomLotteryNumber  = randomLotteryNumber // 10
    theSecondNumOfRandomLotteryNumber = randomLotteryNumber % 10

    #print(randomLotteryNumber)
    lotteryGuessedNumber = int(input("Enter your lottery pick ( 2 digits) or -999 to quit: "))

    firstNumOfGuessedNumber = lotteryGuessedNumber // 10
    secondNumOfGuessedNumber = lotteryGuessedNumber % 10

    # Output
    if (randomLotteryNumber == lotteryGuessedNumber):
        # award is $10,000
        print("Exact match: You win $10,000!")
        print("")
    elif ((theFirstNumOfRandomLotteryNumber == secondNumOfGuessedNumber) and (theSecondNumOfRandomLotteryNumber == firstNumOfGuessedNumber)):
        # award is $3,000
        print("Match all digits : You win $3,000")
        print("")
    elif ((theFirstNumOfRandomLotteryNumber == firstNumOfGuessedNumber) or (theFirstNumOfRandomLotteryNumber == secondNumOfGuessedNumber) or (theSecondNumOfRandomLotteryNumber == firstNumOfGuessedNumber) or (theSecondNumOfRandomLotteryNumber == secondNumOfGuessedNumber)):
        # award is $1,000
        print("Match one digit: You win $1,000")
        print("")
    elif (lotteryGuessedNumber == -999):
        # user wants to quit
        print("")
    else:
        # no match
        print("Sorry no match")
        print("")

## Test run #1 for Homework #2/Program Set #1
## Enter your lottery pick ( 2 digits) or -999 to quit: 34
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 87
## Match one digit: You win $1,000
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 43
## Sorry no match
## 
## Enter your lottery pick ( 2 digits) or -999 to quit: 56
## Match one digit: You win $1,000
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 89
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: -999
##
##
## Test run #2 for Homework #2/Program Set #1
## Enter your lottery pick ( 2 digits) or -999 to quit: 86
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 92
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 74
## Match one digit: You win $1,000
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 59
## Match one digit: You win $1,000
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 49
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: -999
##
##
## Test run #3 for Homework #2/Program Set #1
## Enter your lottery pick ( 2 digits) or -999 to quit: 63
## Match one digit: You win $1,000
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 71
## Match one digit: You win $1,000
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 29
## Exact match: You win $10,000!
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 59
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 41
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: -999
##
##
## Test run #4 for Homework #2/Program Set #1
## Enter your lottery pick ( 2 digits) or -999 to quit: 92
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 48
## Match one digit: You win $1,000
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 29
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 39
## Match one digit: You win $1,000
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 29
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: -999
##
##
## Test run #5 for Homework #2/Program Set #1
## Enter your lottery pick ( 2 digits) or -999 to quit: 83
## Match one digit: You win $1,000
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 38
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 60
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 29
## Match one digit: You win $1,000
##
## Enter your lottery pick ( 2 digits) or -999 to quit: 92
## Sorry no match
##
## Enter your lottery pick ( 2 digits) or -999 to quit: -999

