# Homework 5
# Program Set 1
# Student Name: Bryce Berwald
# Student ID#: 1212962
# Program Description: ...
 
class Loan: 

    # CONSTRUCTOR
    def __init__(self, annualInterestRate = 0.0, numOfYearsForLoan = 0.0, loanAmount = 0.0, borrowersName = ""): 
        '''Doc String Goes Here'''
        self.__annualInterestRate = annualInterestRate
        self.__numOfYearsForLoan = numOfYearsForLoan
        self.__loanAmount = loanAmount
        self.__borrowersName = borrowersName
    

    # SETTERS
    def setAnnualInterestRate(self, rate):
        '''Doc String Goes Here'''
        self.__annualInterestRate = rate


    def setNumberOfYearsForLoan(self, numYears):
        '''Doc String Goes Here'''
        self.__numOfYearsForLoan = numYears


    def setLoanAmount(self, amount):
        '''Doc String Goes Here'''
        self.__loanAmount = amount


    def setBorrowersName(self, name):
        '''Doc String Goes Here'''
        self.__borrowersName = name


    # GETTERS
    def getAnnualInterestRate(self):
        '''Doc String Goes Here'''
        return self.__annualInterestRate


    def getNumberOfYearsForLoan(self):
        '''Doc String Goes Here'''
        return self.__numOfYearsForLoan


    def getLoanAmount(self):
        '''Doc String Goes Here'''
        return self.__loanAmount


    def getBorrowersName(self):
        '''Doc String Goes Here'''
        return self.__borrowersName


    def getMonthlyPayment(self):
        '''Doc String Goes Here'''
        annualRate = self.__annualInterestRate
        numberYears = self.__numOfYearsForLoan
        loanAmount = self.__loanAmount

        monthlyRate = annualRate / 1200
        monthlyPayment = loanAmount * monthlyRate / (1 - (1 / (1 + monthlyRate) ** (numberYears * 12)))

        return monthlyPayment


    def getTotalPayment(self):
        '''Doc String Goes Here'''
        monthlyPayment = self.getMonthlyPayment()
        numberOfYears = self.__numOfYearsForLoan

        totalPayment = monthlyPayment * numberOfYears * 12

        return totalPayment


def main() :
    newLoan = Loan()

    annualRate = float(input("Enter yearly interest rate: "))
    newLoan.setAnnualInterestRate(annualRate)

    numberYears = float(input("Enter number of years as an integer: "))
    newLoan.setNumberOfYearsForLoan(numberYears)

    loanAmount = float(input("Enter loan amount: "))
    newLoan.setLoanAmount(loanAmount)

    borrowersName = str(input("Enter a borrower's name: "))
    newLoan.setBorrowersName(borrowersName)

    print("The loan is for", newLoan.getBorrowersName())
    print("The monthly payment is", format(newLoan.getMonthlyPayment(), ',.2f'))
    print("The total payment is", format(newLoan.getTotalPayment(), ',.2f'))

    LCV = str(input("Do you want to change the loan amount? "))
    while(LCV == 'Y' or LCV == 'y'):
        newLoanAmount = float(input("Enter new loan amount: "))
        newLoan.setLoanAmount(newLoanAmount)
        print("The loan is for", newLoan.getBorrowersName())
        print("The monthly payment is", format(newLoan.getMonthlyPayment(), ',.2f'))
        print("The total payment is", format(newLoan.getTotalPayment(), ',.2f'))
        LCV = str(input("Do you want to change the loan amount? "))
   

if __name__ == "__main__":
    main()
