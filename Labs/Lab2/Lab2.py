# Lab 2
# Question 1
# Student Name: Bryce Berwald
# Description of program: This program will determine someone's eligibility to vote or not,
# giving the user feedback on if they are eligible or how many years are left to go.

# Data/Input
age = int(input("Enter the age: "))

# Processing/Calculations
if age >= 18:
    print("You are eligible to cast your vote.")
else:
    print("You have to wait for another", 18 - age, "years to cast your vote")

## Test run #1 for Question #1
## Enter the age: 10
## You have to wait for another 8 years to cast your vote
##
##
## Test run #2 for Question #1
## Enter the age: 25
## You are eligible to cast your vote.
##
##
## Test run #3 for Question #1
## Enter the age: 18
## You are eligible to cast your vote.
##
## 
## Test run #4 for Question #1
## Enter the age: 17
## You have to wait for another 1 years to cast your vote
##
##
## Test run #5 for Question #1
## Enter the age: 19
## You are eligible to cast your vote.

# Lab 2
# Question 2
# Student Name: Bryce Berwald
# Description of program: This program will determine if a number is even or odd.

# Data/Input
numberFromUser = int(input("Enter any number: "))

# Processing/Calculations/Output
remainder = numberFromUser % 2

if (remainder == 0):
    print(numberFromUser, "is even")
else:
    print(numberFromUser, "is odd")

## Test run #1 for Question #2
## Enter any number: 125
## 125 is odd
##
##
## Test run #2 for Question #2
## Enter any number: 12
## 12 is even
##
##
## Test run #3 for Question #2
## Enter any number: 202
## 202 is even
##
##
## Test run #4 for Question #2
## Enter any number: 199
## 199 is odd
##
##
## Test run #5 for Question #2
## Enter any number: 80
## 80 is even

# Lab 2
# Question 3
# Student Name: Bryce Berwald
# Description of program: This program will determine if the input letter is a vowel or not.

# Data/Input
letter = input("Enter any character: ")

# Processing/Calculations/Output
if (letter == "a" or letter == "A"):
    print(letter, "is a vowel")
elif (letter == "e" or letter == "E"):
    print(letter, "is a vowel")
elif (letter == "i" or letter == "I"):
    print(letter, "is a vowel")
elif (letter == "o" or letter == "O"):
    print(letter, "is a vowel")
elif (letter == "u" or letter == "U"):
    print(letter, "is a vowel")
else:
    print(letter, "is not a vowel")

## Test run #1 for Question #3
## Enter any character: h
## h is not a vowel
##
##
## Test run #2 for Question #3
## Enter any character: e
## e is a vowel
##
##
## Test run #3 for Question #3
## Enter any character: i
## i is a vowel
##
##
## Test run #4 for Question #3
## Enter any character: w
## w is not a vowel
##
##
## Test run #5 for Question #3
## Enter any character: Z
## Z is not a vowel

# Lab 2
# Question 4
# Student Name: Bryce Berwald
# Description of program: This program will determine if the input is a number or a letter.
# And if it's a letter, the program will let us know if it's uppercase or lowercase.

# Data/Input
character = input("Enter any character: ")

# Processing/Calculations/Output
if (character == "a" or character == "A" or character == "b" or character == "B" or character == "c" or character == "C" or character == "d" or character == "D" or character == "e" or character == "E" or character == "f" or character == "F" or character == "g" or character == "G" or character == "h" or character == "H" or character == "i" or character == "I" or character == "j" or character == "J" or character == "k" or character == "K" or character == "l" or character == "L" or character == "m" or character == "M" or character == "n" or character == "N" or character == "o" or character == "O" or character == "p" or character == "P" or character == "q" or character == "Q" or character == "r" or character == "R" or character == "s" or character == "S" or character == "t" or character == "T" or character == "u" or character == "U" or character == "v" or character == "V" or character == "w" or character == "W" or character == "x" or character == "X" or character == "y" or character == "Y" or character == "z" or character == "Z"):
    if (character == "a" or character == "b" or character == "c" or character == "d" or character == "e" or character == "f" or character == "g" or character == "h" or character == "i" or character == "j" or character == "k" or character == "l" or character == "m" or character == "n" or character == "o" or character == "p" or character == "q" or character == "r" or character == "s" or character == "t" or character == "u" or character == "v" or character == "w" or character == "x" or character == "y" or character == "z"):
        print("Lowercase character was entered.")
    elif (character == "A" or character == "B" or character == "C" or character == "D" or character == "E" or character == "F" or character == "G" or character == "H" or character == "I" or character == "J" or character == "K" or character == "L" or character == "M" or character == "N" or character == "O" or character == "P" or character == "Q" or character == "R" or character == "S" or character == "T" or character == "U" or character == "V" or character == "W" or character == "X" or character == "Y" or character == "Z"):
        print("Uppercase character was entered.")
elif (character == "0" or character == "1" or character == "2" or character == "3" or character == "4" or character == "5" or character == "6" or character == "7" or character == "8" or character == "9"):
    print("A number was entered.")
else:
    print("ERROR - Invalid Input!")

## Test run #1 for Question #4
## Enter any character: C
## Uppercase character was entered.
##
##
## Test run #2 for Question #4
## Enter any character: b
## Lowercase character was entered.
##
##
## Test run #3 for Question #4
## Enter any character: 2
## A number was entered.
##
##
## Test run #4 for Question #4
## Enter any character: z
## Lowercase character was entered.
##
##
## Test run #5 for Question #4
## Enter any character: R
## Uppercase character was entered.

# Lab 2
# Question 5
# Student Name: Bryce Berwald
# Description of program: This program will print the number of asterisks the
# user specifies on one line using a while loop.

# Variable & Constant declarations
counter = 0

# Data/Input
howManyStars = int(input("How many stars you want? "))

# Processing/Calculations/Output
while(counter < howManyStars):
    print("*", end='')
    counter = counter + 1

## Test run #1 for Question #5
## How many stars you want? 20
## ********************
##
##
## Test run #2 for Question #5
## How many stars you want? 7
## *******
##
##
## Test run #3 for Question #5
## How many stars you want? 2
## **
##
##
## Test run #4 for Question #5
## How many stars you want? 9
## *********
##
##
## Test run #5 for Question #5
## How many stars you want? 31
## *******************************

# Lab 2
# Question 6
# Student Name: Bryce Berwald
# Description of program: This program will calculate the property tax from the property
# value entered by the user and then outputs it to the screen until sentinel value is entered.

# Variable & Constant declarations
TAX = 0.0065
lotNumber = 0
propertyTax = 0.0

# Processing/Calculations/Input/Output
while(lotNumber != -999):
    print("Enter the property lot number or enter -999 to end ")
    lotNumber = int(input("Enter the lot number: "))

    if (lotNumber != -999):
        propertyValue = float(input("Enter property value: "))
        propertyTax = propertyValue * TAX
        print("Property tax: $", format(propertyTax, '.2f'))

## Test run #1 for Question #6
## Enter the property lot number or enter -999 to end 
## Enter the lot number: 100
## Enter property value: 100000.00
## Property tax: $ 650.00
##
##
## Test run #2 for Question #6
## Enter the property lot number or enter -999 to end 
## Enter the lot number: 200
## Enter property value: 5000.00
## Property tax: $ 32.50
##
##
## Test run #3 for Question #6
## Enter the property lot number or enter -999 to end 
## Enter the lot number: -999
##
##
## Test run #4 for Question #6
## Enter the property lot number or enter -999 to end 
## Enter the lot number: 20
## Enter property value: 90777.77
## Property tax: $ 590.06
##
##
## Test run #5 for Question #6
## Enter the property lot number or enter -999 to end 
## Enter the lot number: 399
## Enter property value: 54809.40
## Property tax: $ 356.26

# Lab 2
# Question 7
# Student Name: Bryce Berwald
# Description of program: This program will take a wholesale cost from the user and determine the
# reail value. If wholesale cost is less than zero, it'll prompt the user for a correction. The
# program will also continue inputting items unless the user says so.

# Variable & Constant declarations
MARKUP_VALUE = 2.5
itemsWholesaleCost = 0.0
anotherItem = "y"

# Input/Processing/Calculations/Output
while (anotherItem == "y" or anotherItem == "Y"):
    itemsWholesaleCost = float(input("Enter the item???s wholesale cost: "))

    while(itemsWholesaleCost < 0):
        itemsWholesaleCost = 0.0
        itemsWholesaleCost = float(input("Enter the correct wholesale cost: "))

    retailPrice = itemsWholesaleCost * MARKUP_VALUE

    print("Retail price is $", format(retailPrice, '.2f'))

    anotherItem = str(input("Do you have another item? (Enter y for yes): "))

## Test run #1 for Question #7
## Enter the item???s wholesale cost: -.50
## Enter the correct wholesale cost: .50
## Retail price is $ 1.25
## Do you have another item? (Enter y for yes): n
##
##
## Test run #2 for Question #7
## Enter the item???s wholesale cost: .75
## Retail price is $ 1.88
## Do you have another item? (Enter y for yes): Y
## Enter the item???s wholesale cost: .50
## Retail price is $ 1.25
## Do you have another item? (Enter y for yes): n
##
##
## Test run #3 for Question #7
## Enter the item???s wholesale cost: -1.90
## Enter the correct wholesale cost: -10.80
## Enter the correct wholesale cost: 25.50
## Retail price is $ 63.75
## Do you have another item? (Enter y for yes): y
## Enter the item???s wholesale cost: 40.00
## Retail price is $ 100.00
## Do you have another item? (Enter y for yes): N
##
##
## Test run #4 for Question #7
## Enter the item???s wholesale cost: .90
## Retail price is $ 2.25
## Do you have another item? (Enter y for yes): n
##
##
## Test run #5 for Question #7
## Enter the item???s wholesale cost: -40
## Enter the correct wholesale cost: 40
## Retail price is $ 100.00
## Do you have another item? (Enter y for yes): n

# Lab 2
# Question 8
# Student Name: Bryce Berwald
# Description of program: This program will output the word 'Barzinger' 5 times next to each other
# using a for loop and the range function.

# Processing/Calculations/Output
for word in range(0, 5):
    print("Barzinger", end='')

## Test run #1 for Question #8 (ONLY TEST CASE)
## BarzingerBarzingerBarzingerBarzingerBarzinger

# Lab 2
# Question 9
# Student Name: Bryce Berwald
# Description of program: This program will ask the user how many numbers they would like
# to add up and uses a for loop to do so.

# Variable & Constant declarations
counter = 0
sum = 0

# Data/Input
howManyNumbers = int(input("How many numbers do you want to add? "))

# Processing/Calculations/Output
for number in range(howManyNumbers):
    print("Enter number", counter + 1, ": ", end='')
    inputNumber = int(input())
    sum = sum + inputNumber
    counter = counter + 1

print("The total is", format(sum, '.1f'))

## Test run #1 for Question #9
## How many numbers do you want to add? 3
## Enter number 1 : 25
## Enter number 2 : 34
## Enter number 3 : 33
## The total is 92.0
##
##
## Test run #2 for Question #9
## How many numbers do you want to add? 3
## Enter number 1 : 70
## Enter number 2 : 30
## Enter number 3 : 20
## The total is 120.0
##
##
## Test run #3 for Question #9
## How many numbers do you want to add? 5
## Enter number 1 : 10
## Enter number 2 : 20
## Enter number 3 : 30
## Enter number 4 : 40
## Enter number 5 : 50
## The total is 150.0
##
##
## Test run #4 for Question #9
## How many numbers do you want to add? 2
## Enter number 1 : 25
## Enter number 2 : 22
## The total is 47.0
##
##
## Test run #5 for Question #9
## How many numbers do you want to add? 1
## Enter number 1 : 10
## The total is 10.0

# Lab 2
# Question 10
# Student Name: Bryce Berwald
# Description of program: This program will convert kph to mph over increments of 10 from
# 60 to 130 mph, outputting the conversions to the console.

# Variable & Constant declarations
KPH_START_VALUE = 60
KPH_END_VALUE = 130
INCREMENT = 10
currentKPH = 60
currentMPH = 0.0

# Processing/Calculations/Output
print("KPH\t MPH")
print("-------------------")
for kph in range(KPH_START_VALUE, KPH_END_VALUE+1, INCREMENT):
    currentMPH = currentKPH * 0.6214
    print(currentKPH, "\t", format(currentMPH, '.1f'))
    currentKPH = currentKPH + INCREMENT

## Test run #1 for Question #10 (ONLY TEST CASE)
## KPH	     MPH
## -------------------
## 60 	     37.3
## 70 	     43.5
## 80 	     49.7
## 90 	     55.9
## 100 	     62.1
## 110 	     68.4
## 120 	     74.6
## 130 	     80.8