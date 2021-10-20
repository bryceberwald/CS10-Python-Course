# Lab 3
# Question 1
# Student Name: Bryce Berwald
# Description of program: This program uses two functions by the main program. The main
# program will call the two functions that will print the number of birds in Texas and 
# number of birds in California.

def Texas()-> None:
    '''This function prints number of birds in Texas'''
    
    # Set Variable to a static value of 5000.
    birds = 5000

    # Print results to the console.
    print("Texas has", birds, "birds")


def California()-> None:
    '''This function prints number of birds in California'''
    
    # Set Variable to a static value of 8000.
    birds = 8000

    #Print results to the console.
    print("California has", birds, "birds")


def main():

    # Call Function Texas()
    Texas()

    # Call Function California()
    California()


if __name__ == "__main__":
    main()

## Test run #1 for Question #1
## Texas has 5000 birds
## California has 8000 birds
##
##
## Test run #2 for Question #1
## Texas has 5000 birds
## California has 8000 birds
##
##
## Test run #3 for Question #1
## Texas has 5000 birds
## California has 8000 birds

# Lab 3
# Question 2
# Student Name: Bryce Berwald
# Description of program: This program will use one function in conjuction  with the
# main program. The main program will call the show_Interest() function to calculate
# and print the resulting value using the default arguments.

def show_Interest(rate = 0.01, period = 10, principal = 10000.00)-> None:
    '''This function will calculate and print interest with default values'''

    # Calculate the interest and store into variable.
    interest = principal * rate * period

    # Display the results in monetary format.
    print("The simple interest will be $", end='') 
    print(format(interest, ',.2f'))


def main():

    # Call function show_Interest()
    show_Interest()


if __name__ == "__main__":
    main()

## Test run #1 for Question #2
## The simple interest will be $1,000.00
##
## 
## Test run #2 for Question #2
## The simple interest will be $1,000.00
##
##
## Test run #3 for Question #2
## The simple interest will be $1,000.00

# Lab 3
# Question 3
# Student Name: Bryce Berwald
# Description of program: This program will use three functions other than main. One function
# will gather input data from the user, returning it to the main program to be used by other
# functions. The trigArea() function will calculate the area. The displayArea() function will
# print our results to the console.

def getData()->int:
    '''This function gets input data from the user'''

    # Get the value of the base from the user.
    base = int(input("Enter the base of your triangle: "))

    # Get the value of the height from the user.
    height = int(input("Enter the height of your triangle: "))

    # Return both values.
    return base, height


def trigArea(base : int, height : int) -> float:
    '''This function calculates the area'''

    # Calculate the area
    area = (base * height) / 2

    # Return the area.
    return area


def displayArea(base : int, height : int, area : float)-> None:
    '''This function will print the desired results'''

    # Display all values to the console for the user.
    print("The base, height, and area are", format(base, '.2f'), format(height, '.2f'), format(area, '.2f'))


def main():

    #Call getData() function and store values in variables respectfully.
    base, height = getData()

    # Call trigArea() function and store calculated value into variable.
    area = trigArea(base, height)

    # Call function to display resulting values to the console.
    displayArea(base, height, area)


if __name__ == "__main__":
    main()

## Test run #1 for Question #3
## Enter the base of your triangle: 10
## Enter the height of your triangle: 5
## The base, height, and area are 10.00 5.00 25.00
##
##
## Test run #2 for Question #3
## Enter the base of your triangle: 2
## Enter the height of your triangle: 3
## The base, height, and area are 2.00 3.00 3.00
##
##
## Test run #3 for Question #3
## Enter the base of your triangle: 7
## Enter the height of your triangle: 7
## The base, height, and area are 7.00 7.00 24.50

# Lab 3
# Question 4
# Student Name: Bryce Berwald
# Description of program: This program uses 3 functions along with main. The main program 
# template has been provided by our instructor and have implemented functions according to main.
# The main program will call all of these functions to recieve the data needed to be used in
# our program.

def get_sales()->float:
    '''This function gets and returns monthly sales'''

    # Get monthly sales from the user.
    monthlySales = float(input("Enter the monthly sales: "))

    # Return monthly sales.
    return monthlySales

def get_advanced_pay()->float:
    '''This function gets and returns advanced pay'''

    # Output some instructions to be displayed to our user.
    print("Enter the amount of advanced pay, or")
    print("enter 0 if no advanced pay was given.")
    
    # Get the advanced pay value from the user.
    advancedPay = float(input("Advanced pay: "))
    
    # Return the advanced pay.
    return advancedPay

def determine_comm_rate(sales : int)->float:
    '''This function determines the commission to be returned'''

    # Conditionals to determine commission rate to be returned.
    if (sales < 10000.00):
        commission = .10
    elif (sales >= 10000.00 and sales < 15000.00):
        commission = .12
    elif (sales >= 15000.00 and sales < 18000.00):
        commission = .14
    elif (sales >= 18000 and sales <= 21999.99):
        commission = .16
    elif (sales > 21999.99):
        commission = .18

    # Return commission rate.
    return commission


# This program calculates a salesperson's pay
def main():
    # Get the amount of sales from user
    sales = get_sales()
    
    # Get the amount of advanced pay from user. 
    advanced_pay = get_advanced_pay()
    
    # Determine the commission rate. 
    comm_rate = determine_comm_rate(sales)

    # Calculate the pay.
    pay = sales * comm_rate - advanced_pay

    # Display the amount of pay.
    print('The pay is $', format(pay, ',.2f'), sep='')
    
    # Determine whether the pay is negative. 
    if pay < 0:
        print('The salesperson must reimburse') 
        print('the company.')

if __name__ == "__main__":
    main()

## Test run #1 for Question #4
## Enter the monthly sales: 14550.00
## Enter the amount of advanced pay, or
## enter 0 if no advanced pay was given.
## Advanced pay: 1000.00
## The pay is $746.00
##
##
## Test run #2 for Question #4
## Enter the monthly sales: 9500
## Enter the amount of advanced pay, or
## enter 0 if no advanced pay was given.
## Advanced pay: 0
## The pay is $950.00
##
##
## Test run #3 for Question #4
## Enter the monthly sales: 12000.00
## Enter the amount of advanced pay, or
## enter 0 if no advanced pay was given.
## Advanced pay: 2000.00
## The pay is $-560.00
## The salesperson must reimburse
## the company.

# Lab 3
# Question 5
# Student Name: Bryce Berwald
# Description of program: This program will use one function in conjuction with main that
# has been provided. Main will call our string_total() function to total/sum all of the
# strings index values to be returned to main. The program will output the final results.

def string_total(number_string : str)->int:
    '''This function calculates the string index values to be returned'''
    
    # Set initial value to zero.
    total = 0

    # Loop through all of string index values, converting to integers for totaling.
    for i in range(0, len(number_string), 1):
        index_value = int(number_string[i])
        total += index_value

    # Return the total value.
    return total


def main():
    # Get a string of numbers as input from the user.
    number_string = input('Enter a sequence of digits with nothing separating them: ')
    
    # Call string_total function, and store the total. 
    total = string_total(number_string)
    
    # Display the total.
    print('The total of the digits in the string you entered is', total)


if __name__ == "__main__":
    main()

## Test run #1 for Question #5
## Enter a sequence of digits with nothing separating them: 4563
## The total of the digits in the string you entered is 18
##
##
## Test run #2 for Question #5
## Enter a sequence of digits with nothing separating them: 653214
## The total of the digits in the string you entered is 21
##
##
## Test run #3 for Question #5
## Enter a sequence of digits with nothing separating them: 888
## The total of the digits in the string you entered is 24