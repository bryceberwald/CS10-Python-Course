# Homework 1
# Program Set 1
# Student Name: Bryce Berwald
# Student ID#: 1212962
# Program Description: This program will determine the monthly and total payment for the loan specified by the user.
# The program will ask the user to input the loan amount, annual interest rate and the number of years to payback the loan.

# Data/Input
annualInterestRate = float(input("Enter annual interest rate, (e.g., 7.25): "))
numberOfYears = int(input("Enter number of year as an integer, (e.g., 5): "))
loanAmount = float(input("Enter loan amount, (e.g., 120000.95): "))

# Processing/Calculations
monthlyInterestRate = annualInterestRate / 1200
monthlyPayment = (loanAmount * monthlyInterestRate) / (1 - 1 / (1 + monthlyInterestRate)**(numberOfYears * 12))
totalPayment = monthlyPayment * numberOfYears * 12

# Output
print("\n\nThe monthly payment is", format(monthlyPayment, ',.2f'))
print("The total payment is", format(totalPayment, ',.2f'))

## Test run #1 for Homework #1/Program Set #1
## Enter annual interest rate, (e.g., 7.25): 4.5
## Enter number of year as an integer, (e.g., 5): 30
## Enter loan amount, (e.g., 120000.95): 350000.50
##
##
## The monthly payment is 1,773.40
## The total payment is 638,424.40
##
##
## Test run #2 for Homework #1/Program Set #1
## Enter annual interest rate, (e.g., 7.25): 2.5
## Enter number of year as an integer, (e.g., 5): 10
## Enter loan amount, (e.g., 120000.95): 200300
##
##
## The monthly payment is 1,888.23
## The total payment is 226,587.14
##
##
## Test run #3 for Homework #1/Program Set #1
## Enter annual interest rate, (e.g., 7.25): 4.25
## Enter number of year as an integer, (e.g., 5): 20
## Enter loan amount, (e.g., 120000.95): 500250
##
##
## The monthly payment is 3,097.72
## The total payment is 743,452.90
## 
##
## Test run #4 for Homework #1/Program Set #1
## Enter annual interest rate, (e.g., 7.25): 3.10
## Enter number of year as an integer, (e.g., 5): 5
## Enter loan amount, (e.g., 120000.95): 80000
##
##
## The monthly payment is 1,441.05
## The total payment is 86,463.19
##
##
## Test run #5 for Homework #1/Program Set #1
## Enter annual interest rate, (e.g., 7.25): 1.75
## Enter number of year as an integer, (e.g., 5): 5
## Enter loan amount, (e.g., 120000.95): 15000
##
##
## The monthly payment is 261.28
## The total payment is 15,676.75