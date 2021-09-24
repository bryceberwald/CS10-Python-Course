# Homework 1
# Program Set 2
# Student Name: Bryce Berwald
# Student ID#: 1212962
# Program Description: This program will ask the user a series of questions that will help our program
# calculate whether or not they have made money with a certain stock or not.

# Data/Input
stockName = input("Enter Stock Name: ")
numberOfShares = float(input("Enter the number of shares: "))
puchasePrice = float(input("Enter the purchase price: "))
sellPrice = float(input("Enter selling price: "))
commission = float(input("Enter Commission: "))

# Processing/Calculations
amountPaidForStock = numberOfShares * puchasePrice
commissionPaidOnPurchase = amountPaidForStock * commission
stockSoldAmount = numberOfShares * sellPrice
commissionPaidOnSoldStock = stockSoldAmount * commission

profitOrLoss = (stockSoldAmount - commissionPaidOnSoldStock) - (amountPaidForStock + commissionPaidOnPurchase)

# Output
print("\n\nAmount paid for the stock:          $", format(amountPaidForStock, '13,.2f'))
print("Commission paid on the purchase:    $", format(commissionPaidOnPurchase, '13,.2f'))
print("Amount the stock sold for:          $", format(stockSoldAmount, '13,.2f'))
print("Commission paid on the sale:        $", format(commissionPaidOnSoldStock, '13,.2f'))
print("Profit (or loss if negative):       $", format(profitOrLoss, '13,.2f'))

## Test run #1 for Homework #1/Program Set #2
## Enter Stock Name: Kaplack, Inc.
## Enter the number of shares: 10000
## Enter the purchase price: 33.92
## Enter selling price: 35.92
## Enter Commission: 0.04
##
##
## Amount paid for the stock:          $    339,200.00
## Commission paid on the purchase:    $     13,568.00
## Amount the stock sold for:          $    359,200.00
## Commission paid on the sale:        $     14,368.00
## Profit (or loss if negative):       $     -7,936.00
##
##
## Test run #2 for Homework #1/Program Set #2
## Enter Stock Name: IBM
## Enter the number of shares: 15000
## Enter the purchase price: 50.25
## Enter selling price: 100.20
## Enter Commission: 0.02
##
##
## Amount paid for the stock:          $    753,750.00
## Commission paid on the purchase:    $     15,075.00
## Amount the stock sold for:          $  1,503,000.00
## Commission paid on the sale:        $     30,060.00
## Profit (or loss if negative):       $    704,115.00
##
##
## Test run #3 for Homework #1/Program Set #2
## Enter Stock Name: ADA 
## Enter the number of shares: 1000
## Enter the purchase price: 0.05
## Enter selling price: 3.00
## Enter Commission: 0.02
##
##
## Amount paid for the stock:          $         50.00
## Commission paid on the purchase:    $          1.00
## Amount the stock sold for:          $      3,000.00
## Commission paid on the sale:        $         60.00
## Profit (or loss if negative):       $      2,889.00
##
##
## Test run #4 for Homework #1/Program Set #2
## Enter Stock Name: AAPL
## Enter the number of shares: 500
## Enter the purchase price: 125.00
## Enter selling price: 153.65
## Enter Commission: 0.10
##
##
## Amount paid for the stock:          $     62,500.00
## Commission paid on the purchase:    $      6,250.00
## Amount the stock sold for:          $     76,825.00
## Commission paid on the sale:        $      7,682.50
## Profit (or loss if negative):       $        392.50
##
##
## Test run #5 for Homework #1/Program Set #2
## Enter Stock Name: MSFT
## Enter the number of shares: 92
## Enter the purchase price: 190.00
## Enter selling price: 301.15
## Enter Commission: 0.25
##
##
## Amount paid for the stock:          $     17,480.00
## Commission paid on the purchase:    $      4,370.00
## Amount the stock sold for:          $     27,705.80
## Commission paid on the sale:        $      6,926.45
## Profit (or loss if negative):       $     -1,070.65