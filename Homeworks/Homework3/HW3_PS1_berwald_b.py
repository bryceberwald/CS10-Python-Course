# Homework 3
# Program Set 1
# Student Name: Bryce Berwald
# Student ID#: 1212962
# Program Description: This program is a continuation of Homework #1, Program Set #2. This
# program differs by having functions implemented instead. This program has three functions
# other than main. One function for gathering our users input data. One function for calculating
# the values needed based on the users input values. The final function will display our results
# to the console and nothing is returned by this function. The program will continue to iterate
# until the user specifies a 'n' when being asked if they'd like to continue entering their
# stock information.

def getInputData()->(str, float, float, float, float):
    '''This function will get input data to be returned'''

    # Data/Input
    stockName = str(input("\nEnter Stock Name: "))
    numberOfShares = float(input("Enter the number of shares: "))
    purchasePrice = float(input("Enter the purchase price: "))
    sellPrice = float(input("Enter selling price: "))
    commission = float(input("Enter Commission: "))

    # Return the input data.
    return stockName, numberOfShares, purchasePrice, sellPrice, commission


def performCalculations(numberOfShares : float, purchasePrice : float, sellPrice : float, commission : float):
    '''This function will perform calculations and return the values'''
    
    # Processing/Calculations
    amountPaidForStock = numberOfShares * purchasePrice
    commissionPaidOnPurchase = amountPaidForStock * commission
    stockSoldAmount = numberOfShares * sellPrice
    commissionPaidOnSoldStock = stockSoldAmount * commission

    # Return the calculated values.
    return amountPaidForStock, commissionPaidOnPurchase, stockSoldAmount, commissionPaidOnSoldStock


def displayResults(stockName : str, amountPaidForStock : float, commissionPaidOnPurchase : float, stockSoldAmount : float, commissionPaidOnSoldStock : float, profitOrLoss : float)->None:
    '''This function will output the desired results to the console'''
    
    # Output Results
    print("\n\nStock name :", stockName)
    print("Amount paid for the stock:          $", format(amountPaidForStock, '13,.2f'))
    print("Commission paid on the purchase:    $", format(commissionPaidOnPurchase, '13,.2f'))
    print("Amount the stock sold for:          $", format(stockSoldAmount, '13,.2f'))
    print("Commission paid on the sale:        $", format(commissionPaidOnSoldStock, '13,.2f'))
    print("Profit (or loss if negative):       $", format(profitOrLoss, '13,.2f'), "\n")


def main():

    # Set variable's inital value to 'y'.
    execution = "y"

    # Loop until the user specifies with 'n'.
    while (execution.lower() == 'y'):

        # Ask the user whether or not they'd like to proceed with entering stock information.
        execution = str(input("Enter your stock information? Type 'y' for yes, or 'n' for no: "))

        # Only executed if the user specifies with 'y'.
        if (execution.lower() == 'y'):
            
            # Call getInputData() function and store values into variables respectfully.
            stockName, numberOfShares, purchasePrice, sellPrice, commission = getInputData()

            # Call performCalculations() function and store values into variables respectfully.
            amountPaidForStock, commissionPaidOnPurchase, stockSoldAmount, commissionPaidOnSoldStock = performCalculations(numberOfShares, purchasePrice, sellPrice, commission)

            # Calculate whether there was a profit or a loss and store into variable.
            profitOrLoss = (stockSoldAmount - commissionPaidOnSoldStock) - (amountPaidForStock + commissionPaidOnPurchase)

            # Call function to output the final results concerning the stock to the console.
            displayResults(stockName, amountPaidForStock, commissionPaidOnPurchase, stockSoldAmount, commissionPaidOnSoldStock, profitOrLoss)


if __name__ == "__main__":
    main()

## Test run #1 for Homework #3/Program Set #1
## Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
## Enter Stock Name: Kaplack, Inc.
## Enter the number of shares: 10000
## Enter the purchase price: 33.92
## Enter selling price: 35.92
## Enter Commission: 0.04
##
##
## Stock name : Kaplack, Inc.
## Amount paid for the stock:          $    339,200.00
## Commission paid on the purchase:    $     13,568.00
## Amount the stock sold for:          $    359,200.00
## Commission paid on the sale:        $     14,368.00
## Profit (or loss if negative):       $     -7,936.00 
##
## Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
## Enter Stock Name: IBM
## Enter the number of shares: 15000
## Enter the purchase price: 50.25
## Enter selling price: 100.20
## Enter Commission: 0.02
##
##
## Stock name : IBM
## Amount paid for the stock:          $    753,750.00
## Commission paid on the purchase:    $     15,075.00
## Amount the stock sold for:          $  1,503,000.00
## Commission paid on the sale:        $     30,060.00
## Profit (or loss if negative):       $    704,115.00 
##
## Enter your stock information? Type 'y' for yes, or 'n' for no: n
## >>> 
##
##
## Test run #2 for Homework #3/Program Set #1
## Enter your stock information? Type 'y' for yes, or 'n' for no: n
## >>> 
##
##
## Test run #3 for Homework #3/Program Set #1
## Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
## Enter Stock Name: AAPL
## Enter the number of shares: 500
## Enter the purchase price: 121.10
## Enter selling price: 148.76
## Enter Commission: 0.02
##
##
## Stock name : AAPL
## Amount paid for the stock:          $     60,550.00
## Commission paid on the purchase:    $      1,211.00
## Amount the stock sold for:          $     74,380.00
## Commission paid on the sale:        $      1,487.60
## Profit (or loss if negative):       $     11,131.40 
##
## Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
## Enter Stock Name: GOOGL
## Enter the number of shares: 1800
## Enter the purchase price: 1200.00
## Enter selling price: 2864.74
## Enter Commission: 0.07
##
##
## Stock name : GOOGL
## Amount paid for the stock:          $  2,160,000.00
## Commission paid on the purchase:    $    151,200.00
## Amount the stock sold for:          $  5,156,532.00
## Commission paid on the sale:        $    360,957.24
## Profit (or loss if negative):       $  2,484,374.76 
##
## Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
## Enter Stock Name: ADA
## Enter the number of shares: 20000
## Enter the purchase price: 0.05
## Enter selling price: 2.11
## Enter Commission: 0.05
##
##
## Stock name : ADA
## Amount paid for the stock:          $      1,000.00
## Commission paid on the purchase:    $         50.00
## Amount the stock sold for:          $     42,200.00
## Commission paid on the sale:        $      2,110.00
## Profit (or loss if negative):       $     39,040.00 
##
## Enter your stock information? Type 'y' for yes, or 'n' for no: n
## >>> 
##
##
## Test run #4 for Homework #3/Program Set #1
## Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
## Enter Stock Name: TSLA
## Enter the number of shares: 400
## Enter the purchase price: 678.90
## Enter selling price: 864.27
## Enter Commission: 0.08
##
##
## Stock name : TSLA
## Amount paid for the stock:          $    271,560.00
## Commission paid on the purchase:    $     21,724.80
## Amount the stock sold for:          $    345,708.00
## Commission paid on the sale:        $     27,656.64
## Profit (or loss if negative):       $     24,766.56 
##
## Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
## Enter Stock Name: HD
## Enter the number of shares: 100
## Enter the purchase price: 239.00
## Enter selling price: 357.99
## Enter Commission: 0.10
##
##
## Stock name : HD
## Amount paid for the stock:          $     23,900.00
## Commission paid on the purchase:    $      2,390.00
## Amount the stock sold for:          $     35,799.00
## Commission paid on the sale:        $      3,579.90
## Profit (or loss if negative):       $      5,929.10 
##
## Enter your stock information? Type 'y' for yes, or 'n' for no: n
## >>> 
##
##
## Test run #5 for Homework #3/Program Set #1
## Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
## Enter Stock Name: FB
## Enter the number of shares: 200
## Enter the purchase price: 341.06
## Enter selling price: 339.99
## Enter Commission: 0.04
##
##
## Stock name : FB
## Amount paid for the stock:          $     68,212.00
## Commission paid on the purchase:    $      2,728.48
## Amount the stock sold for:          $     67,998.00
## Commission paid on the sale:        $      2,719.92
## Profit (or loss if negative):       $     -5,662.40 
##
## Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
## Enter Stock Name: TWTR
## Enter the number of shares: 100
## Enter the purchase price: 67.26
## Enter selling price: 66.11
## Enter Commission: 0
##
##
## Stock name : TWTR
## Amount paid for the stock:          $      6,726.00
## Commission paid on the purchase:    $          0.00
## Amount the stock sold for:          $      6,611.00
## Commission paid on the sale:        $          0.00
## Profit (or loss if negative):       $       -115.00 
##
## Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
## Enter Stock Name: ADA
## Enter the number of shares: 10000
## Enter the purchase price: 0.05
## Enter selling price: 2.11
## Enter Commission: 0
##
##
## Stock name : ADA
## Amount paid for the stock:          $        500.00
## Commission paid on the purchase:    $          0.00
## Amount the stock sold for:          $     21,100.00
## Commission paid on the sale:        $          0.00
## Profit (or loss if negative):       $     20,600.00 
##
## Enter your stock information? Type 'y' for yes, or 'n' for no: n
## >>> 