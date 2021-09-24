# Lab 2
# Question 1
# Student Name: Bryce Berwald
# Description of program: This program will determine someone's eligibility to vote or not,
# giving the user feedback on if they are eligible or how many years are left to go.

# Data/Input
#age = int(input("Enter the age: "))

# Processing/Calculations
#if age >= 18:
#    print("You are eligible to cast your vote.")
#else:
#    print("You have to wait for another", 18 - age, "years to cast your vote")

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
#numberFromUser = int(input("Enter any number: "))

# Processing/Calculations/Output
#remainder = numberFromUser % 2

#if (remainder == 0):
#    print(numberFromUser, "is even")
#else:
#    print(numberFromUser, "is odd")

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
#letter = input("Enter any character: ")

# Processing/Calculations/Output
#if (letter == "a" or letter == "A"):
#    print(letter, "is a vowel")
#elif (letter == "e" or letter == "E"):
#    print(letter, "is a vowel")
#elif (letter == "i" or letter == "I"):
#    print(letter, "is a vowel")
#elif (letter == "o" or letter == "O"):
#    print(letter, "is a vowel")
#elif (letter == "u" or letter == "U"):
#    print(letter, "is a vowel")
#else:
#    print(letter, "is not a vowel")

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

# Variable & Constant declarations

# Data/Input
character = str(input("Enter any character: "))

# Processing/Calculations
if (character == "a" or "A"):
    if (character == "a"):
        print("Lowercase character was entered.")
    elif (character == "A"):
        print("Uppercase character was entered.")
else:
    print("Error")
# Output





