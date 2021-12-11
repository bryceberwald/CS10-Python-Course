# Homework 5
# Program Set 1
# Student Name: Bryce Berwald
# Student ID#: 1212962
# Program Description: This program will allow a user to enter a series of inputs to calculate loan
# values needed by this program. This program creates a class with four getter and four setter class
# methods which will be invoked to get and set the private class sttributes. The class named 'Loan' 
# also has two additional methods which will be used to calculate and return the monthly and total
# payment values. The program will continue to loop for new loan values until the user decides to
# quit with the enter key.
 
# Class Name: Loan
# Description: This class will be used by the main program to calculate loan values for
# our user. The class consists of 4 getters & 4 setters, along with two other methods to
# access the private attributes which are assigned default values initially by the constructor.
class Loan: 

    # Constructor Class Method
    def __init__(self, annualInterestRate = 0.0, numOfYearsForLoan = 0.0, loanAmount = 0.0, borrowersName = ""): 
        '''Constructor function assigns default values to private variables'''
        self.__annualInterestRate = annualInterestRate
        self.__numOfYearsForLoan = numOfYearsForLoan
        self.__loanAmount = loanAmount
        self.__borrowersName = borrowersName
    

    # Setter/Mutator Class Methods
    def setAnnualInterestRate(self, rate : float)->None:
        '''Setter Function will set the annual interest rate'''
        self.__annualInterestRate = rate


    def setNumberOfYearsForLoan(self, numYears : float)->None:
        '''Setter Function will set the number of years for a loan'''
        self.__numOfYearsForLoan = numYears


    def setLoanAmount(self, amount : float)->None:
        '''Setter Function will set the loan amount'''
        self.__loanAmount = amount


    def setBorrowersName(self, name : str)->None:
        '''Setter Function will set the name of the loan borrower'''
        self.__borrowersName = name


    # Getter/Accessor Class Methods
    def getAnnualInterestRate(self)->float:
        '''Getter Function will return the annual interest rate'''
        return self.__annualInterestRate


    def getNumberOfYearsForLoan(self)->float:
        '''Getter Function will return the number of years for a loan'''
        return self.__numOfYearsForLoan


    def getLoanAmount(self)->float:
        '''Getter Function will return the loan amount'''
        return self.__loanAmount


    def getBorrowersName(self)->str:
        '''Getter Function will return the name of the loan borrower'''
        return self.__borrowersName


    # Public Class Methods
    def getMonthlyPayment(self)->float:
        '''Function will calculate the monthly payment to be returned'''
        annualRate = self.__annualInterestRate
        numberYears = self.__numOfYearsForLoan
        loanAmount = self.__loanAmount

        monthlyRate = annualRate / 1200
        monthlyPayment = loanAmount * monthlyRate / (1 - (1 / (1 + monthlyRate) ** (numberYears * 12)))

        return monthlyPayment


    def getTotalPayment(self)->float:
        '''Function will calculate the total payment to be returned'''
        monthlyPayment = self.getMonthlyPayment()
        numberOfYears = self.__numOfYearsForLoan

        totalPayment = monthlyPayment * numberOfYears * 12

        return totalPayment


def main():
    # Create an instance of the class named "Loan".
    newLoan = Loan()

    # Ask the user for a input value for annual interest rate.
    annualRate = float(input("Enter yearly interest rate: "))

    # Assign users value with class method.
    newLoan.setAnnualInterestRate(annualRate)

    # Ask the user for a input value for number of years for loan.
    numberYears = float(input("Enter number of years as an integer: "))

    # Assign users value with class method.
    newLoan.setNumberOfYearsForLoan(numberYears)

    # Ask the user for a input value for the loan amount.
    loanAmount = float(input("Enter loan amount: "))

    # Assign users value with class method.
    newLoan.setLoanAmount(loanAmount)

    # Ask the user for the loan borrowers name.
    borrowersName = str(input("Enter a borrower's name: "))

    # Assign users value with class method.
    newLoan.setBorrowersName(borrowersName)

    # Display the resulting loan values calculated from private class attributes.
    print("The loan is for", newLoan.getBorrowersName())
    print("The monthly payment is", format(newLoan.getMonthlyPayment(), ',.2f'))
    print("The total payment is", format(newLoan.getTotalPayment(), ',.2f'))

    # Create a loop control variable, which is assigned the users input.
    LCV = str(input("Do you want to change the loan amount? Y for yes or enter to quit "))

    # Loop while users input is a yes for an answer.
    while(LCV == 'Y' or LCV == 'y'):

        # Ask user for a new loan amount.
        newLoanAmount = float(input("Enter new loan amount: "))

        # Assign users value with class method.
        newLoan.setLoanAmount(newLoanAmount)

        # Display the new resulting loan values to the console.
        print("The loan is for", newLoan.getBorrowersName())
        print("The monthly payment is", format(newLoan.getMonthlyPayment(), ',.2f'))
        print("The total payment is", format(newLoan.getTotalPayment(), ',.2f'))

        # Ask the user if they would like to enter another loan again.
        LCV = str(input("Do you want to change the loan amount? Y for yes or enter to quit "))
   

if __name__ == "__main__":
    main()

## Test run #1 for Homework #5/Program Set #1
## Enter yearly interest rate: 2.5
## Enter number of years as an integer: 5
## Enter loan amount: 1000.00
## Enter a borrower's name: John Jones
## The loan is for John Jones
## The monthly payment is 17.75
## The total payment is 1,064.84
## Do you want to change the loan amount? Y for yes or enter to quit y
## Enter new loan amount: 5000
## The loan is for John Jones
## The monthly payment is 88.74
## The total payment is 5,324.21
## Do you want to change the loan amount? Y for yes or enter to quit 
## >>> 
##
##
## Test run #2 for Homework #5/Program Set #1
## Enter yearly interest rate: 1.25
## Enter number of years as an integer: 2
## Enter loan amount: 2500.00
## Enter a borrower's name: Bryce Berwald
## The loan is for Bryce Berwald
## The monthly payment is 105.53
## The total payment is 2,532.68
## Do you want to change the loan amount? Y for yes or enter to quit y
## Enter new loan amount: 3000.00
## The loan is for Bryce Berwald
## The monthly payment is 126.63
## The total payment is 3,039.22
## Do you want to change the loan amount? Y for yes or enter to quit 
## >>> 
##
##
## Test run #3 for Homework #5/Program Set #1
## Enter yearly interest rate: 4.8
## Enter number of years as an integer: 7
## Enter loan amount: 170777.77
## Enter a borrower's name: Lucky Luke
## The loan is for Lucky Luke
## The monthly payment is 2,397.74
## The total payment is 201,410.24
## Do you want to change the loan amount? Y for yes or enter to quit Y
## Enter new loan amount: 777000.77
## The loan is for Lucky Luke
## The monthly payment is 10,909.19
## The total payment is 916,371.67
## Do you want to change the loan amount? Y for yes or enter to quit 
## >>> 
##
##
## Test run #4 for Homework #5/Program Set #1
## Enter yearly interest rate: 3.70
## Enter number of years as an integer: 12
## Enter loan amount: 1000
## Enter a borrower's name: jeff
## The loan is for jeff
## The monthly payment is 8.61
## The total payment is 1,239.89
## Do you want to change the loan amount? Y for yes or enter to quit y
## Enter new loan amount: 3000
## The loan is for jeff
## The monthly payment is 25.83
## The total payment is 3,719.67
## Do you want to change the loan amount? Y for yes or enter to quit Y
## Enter new loan amount: 8000
## The loan is for jeff
## The monthly payment is 68.88
## The total payment is 9,919.12
## Do you want to change the loan amount? Y for yes or enter to quit 
## >>> 
##
##
## Test run #5 for Homework #5/Program Set #1
## Enter yearly interest rate: 7.25
## Enter number of years as an integer: 800
## Enter loan amount: 1000100.99
## Enter a borrower's name: Millionaire Mike
## The loan is for Millionaire Mike
## The monthly payment is 6,042.28
## The total payment is 58,005,857.42
## Do you want to change the loan amount? Y for yes or enter to quit Y
## Enter new loan amount: 2000000
## The loan is for Millionaire Mike
## The monthly payment is 12,083.33
## The total payment is 116,000,000.00
## Do you want to change the loan amount? Y for yes or enter to quit Y
## Enter new loan amount: 3000000
## The loan is for Millionaire Mike
## The monthly payment is 18,125.00
## The total payment is 174,000,000.00
## Do you want to change the loan amount? Y for yes or enter to quit y
## Enter new loan amount: 10222333.00
## The loan is for Millionaire Mike
## The monthly payment is 61,759.93
## The total payment is 592,895,314.00
## Do you want to change the loan amount? Y for yes or enter to quit 
## >>> 