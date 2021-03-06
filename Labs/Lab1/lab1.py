# Lab 1
# Question 4
# Student Name: Bryce Berwald
# Description of program: This program will read the radius & length of a cylinder and find the area & volume.

# Variable & Constant declarations
PI = 3.141

# Data/Input
cylinderRadius = float(input("Enter the radius of a cylinder: "))
cylinderLength = float(input("Enter the length of a cylinder: "))

# Processing/Calculations
area = cylinderRadius * cylinderRadius * PI
volume = area * cylinderLength

# Output
print("The area is", area)
print("The volume is", volume)

## Test run #1 for Question #4
## Enter the radius of a cylinder: 5.5
## Enter the length of a cylinder: 12
## The area is 95.01525
## The volume is 1140.183
##
##
## Test run #2 for Question #4
## Enter the radius of a cylinder: 7
## Enter the length of a cylinder: 14
## The area is 153.909
## The volume is 2154.7259999999997
##
##
## Test run #3 for Question #4
## Enter the radius of a cylinder: 8
## Enter the length of a cylinder: 19
## The area is 201.024
## The volume is 3819.456
##
##
## Test run #4 for Question #4
## Enter the radius of a cylinder: 17
## Enter the length of a cylinder: 10
## The area is 907.749
## The volume is 9077.49
##
##
## Test run #5 for Question #4
## Enter the radius of a cylinder: 5
## Enter the length of a cylinder: 11
## The area is 78.525
## The volume is 863.7750000000001

# Lab 1
# Question 5
# Student Name: Bryce Berwald
# Description of program: This program will input the amount of total sales to determine the profit made.

# Variable & Constant declarations
profitMargin = .24

# Data/Input
totalSales = float(input("Enter the projected total sales: "))

# Processing/Calculations
profitMade = totalSales * profitMargin

# Output
print("The profit made from this amount:", format(profitMade, '.2f'))

## Test run #1 for Question #5
## Enter the projected total sales: 1250.00
## The profit made from this amount: 300.00
##
##
## Test run #2 for Question #5
## Enter the projected total sales: 2100.00
## The profit made from this amount: 504.00
##
##
## Test run #3 for Question #5
## Enter the projected total sales: 5000.00
## The profit made from this amount: 1200.00
##
##
## Test run #4 for Question #5
## Enter the projected total sales: 12500.50
## The profit made from this amount: 3000.12
##
##
## Test run #5 for Question #5
## Enter the projected total sales: 7000.00 
## The profit made from this amount: 1680.00

# Lab 1
# Question 6
# Student Name: Bryce Berwald
# Description of program: This program will determine the quantity of ingredients needed by the amount of cookies being baked.

# Variable & Constant declarations
CUPS_OF_SUGAR = 1.5
CUPS_OF_BUTTER = 1
CUPS_OF_FLOUR = 2.75

# Data/Input
cookieAmount = float(input("Enter the number of cookies: "))

# Processing/Calculations
ratio = cookieAmount / 48

sugarNeeded = CUPS_OF_SUGAR * ratio
butterNeeded = CUPS_OF_BUTTER * ratio
flourNeeded = CUPS_OF_FLOUR * ratio

# Output
print("\n\nTo make", cookieAmount, "cookies, you will need:")
print(format(sugarNeeded, '.2f'), "cups of sugar")
print(format(butterNeeded, '.2f'), "cups of butter")
print(format(flourNeeded, '.2f'), "cups of flour")

## Test run #1 for Question #6
## Enter the number of cookies: 56
##
##
## To make 56.0 cookies, you will need:
## 1.75 cups of sugar
## 1.17 cups of butter
## 3.21 cups of flour
##
##
## Test run #2 for Question #6
## Enter the number of cookies: 70
##
##
## To make 70.0 cookies, you will need:
## 2.19 cups of sugar
## 1.46 cups of butter
## 4.01 cups of flour
##
##
## Test run #3 for Question #6
## Enter the number of cookies: 220
##
##
## To make 220.0 cookies, you will need:
## 6.88 cups of sugar
## 4.58 cups of butter
## 12.60 cups of flour
##
##
## Test run #4 for Question #6
## Enter the number of cookies: 12
##
##
## To make 12.0 cookies, you will need:
## 0.38 cups of sugar
## 0.25 cups of butter
## 0.69 cups of flour
##
##
## Test run #5 for Question #6
## Enter the number of cookies: 777
##
##
## To make 777.0 cookies, you will need:
## 24.28 cups of sugar
## 16.19 cups of butter
## 44.52 cups of flour

# Lab 1
# Question 7
# Student Name: Bryce Berwald
# Description of program: This program will input a four digit number and reverse the order to be printed using math.

# Data/Input
fourDigitNumber = int(input("Enter an integer: "))

# Processing/Calculations
firstNumber = fourDigitNumber // 1000
remainder = fourDigitNumber % 1000
secondNumber = remainder // 100
remainder = remainder % 100
thirdNumber = remainder // 10
fourthNumber = remainder % 10

# Output
print(fourthNumber)
print(thirdNumber)
print(secondNumber)
print(firstNumber)

## Test run #1 for Question #7
## Enter an integer: 3125
## 5
## 2
## 1
## 3
##
##
## Test run #2 for Question #7
## Enter an integer: 8190
## 0
## 9
## 1
## 8
##
##
## Test run #3 for Question #7
## Enter an integer: 1234
## 4
## 3
## 2
## 1
##
##
## Test run #4 for Question #7
## Enter an integer: 7293
## 3
## 9
## 2
## 7
##
##
## Test run #5 for Question #7
## Enter an integer: 0502
## 2
## 0
## 5
## 0

# Lab 1
# Question 8
# Student Name: Bryce Berwald
# Description of program: This program will input 'm' allowing the program to determine gravitational force against oneself.

# Variable & Constant declarations
UNIVERSAL_GRAVITATIONAL_FORCE = 6.67300 * 10**-11    # G
EARTHS_RADIUS = 6378 * 10**3                         # r
EARTHS_MASS = 5.9742 * 10**24                        # m1

# Data/Input
massFromUser = float(input("Enter a mass in kg: "))  # m

# Processing/Calculations
# Formula: g = [G (m1) (m) / (r^2) ] / m
g = (UNIVERSAL_GRAVITATIONAL_FORCE * EARTHS_MASS * massFromUser / EARTHS_RADIUS**2) / massFromUser


# Output
print("\n\nThe resulting value of g is", format(g, '.4f'), "which is close to earths gravitational force.")

## Test run #1 for Question #8
## Enter a mass in kg: 30
##
##
## The resulting value of g is 9.8001 which is close to earths gravitational force.
##
##
## Test run #2 for Question #8
## Enter a mass in kg: 50
##
##
## The resulting value of g is 9.8001 which is close to earths gravitational force.
##
## Test run #3 for Question #8
## Enter a mass in kg: 2900
##
##
## The resulting value of g is 9.8001 which is close to earths gravitational force.
##
##
## Test run #4 for Question #8
## Enter a mass in kg: 1000000
##
##
## The resulting value of g is 9.8001 which is close to earths gravitational force.
##
##
## Test run #5 for Question #8
## Enter a mass in kg: 77
##
##
## The resulting value of g is 9.8001 which is close to earths gravitational force.



