# Homework 2
# Program Set 2
# Student Name: Bryce Berwald
# Student ID#: 1212962
# Program Description: This program will prompt the user to enter an income value. If the income value
# is greater than or equal to zero the program will continue. The program will also loop until a
# negative input value for the income is entered. The program will calculate the taxable income
# based on the 2017 and older and 2018 and newer tax brackets. The difference between the two tax
# brackets will be calculated and the percentage of the difference as well. Finally, the results
# will be displayed via the console.

# Data/Input
incomeAmount = int(input("Enter income as an integer with no commas: "))

# Loop until negative while is entered.
while (incomeAmount >= 0):

    # Calculate 2017 and older tax bracket
    incomeAmount2017 = incomeAmount

    # Variables for 2017 & older tax bracket calculations
    tenPercentTaxable2017 = 0
    fifteenPercentTaxable2017 = 0
    twentyFivePercentTaxable2017 = 0
    twentyEightPercentTaxable2017 = 0
    thirtyThreePercentTaxable2017 = 0
    thirtyFivePercentTaxable2017 = 0
    thirtyNinePointSixPercentTaxable2017 = 0

    # 10 Percent (2017)
    if (incomeAmount2017 > 9325):
        tenPercentTaxable2017 = 9325 * .1
        incomeAmount2017 = incomeAmount2017 - 9325

        # 15 Percent (2017)
        if (incomeAmount2017 > 28625):
            fifteenPercentTaxable2017 = 28625 * .15
            incomeAmount2017 = incomeAmount2017 - 28625

            # 25 Percent (2017)
            if (incomeAmount2017 > 53950):
                twentyFivePercentTaxable2017 = 53950 * .25
                incomeAmount2017 = incomeAmount2017 - 53950

                # 28 Percent (2017)
                if (incomeAmount2017 > 99750):
                    twentyEightPercentTaxable2017 = 99750 * .28
                    incomeAmount2017 = incomeAmount2017 - 99750

                    # 33 Percent (2017)
                    if (incomeAmount2017 > 225050):
                        thirtyThreePercentTaxable2017 = 225050 * .33
                        incomeAmount2017 = incomeAmount2017 - 225050

                        # 35 Percent (2017)
                        if (incomeAmount2017 > 1700):
                            thirtyFivePercentTaxable2017 = 1700 * .35
                            incomeAmount2017 = incomeAmount2017 - 1700

                            # 39.6 Percent (2017)
                            thirtyNinePointSixPercentTaxable2017 = incomeAmount2017 * .396

                        # 35%
                        else: 
                            thirtyFivePercentTaxable2017 = incomeAmount2017 * .35
                    # 33%
                    else:
                        thirtyThreePercentTaxable2017 = incomeAmount2017 * .33
                # 28%
                else:
                    twentyEightPercentTaxable2017 = incomeAmount2017 * .28
            # 25%
            else:
                twentyFivePercentTaxable2017 = incomeAmount2017 * .25
        #15%
        else:
            fifteenPercentTaxable2017 = incomeAmount2017 * .15
    # 10%
    else:
        tenPercentTaxable2017 = incomeAmount2017 * .1


    # Total Tax for 2017 and older tax bracket is stored in this variable.
    totalTax2017 = tenPercentTaxable2017 + fifteenPercentTaxable2017 + twentyFivePercentTaxable2017 + twentyEightPercentTaxable2017 + thirtyThreePercentTaxable2017 + thirtyFivePercentTaxable2017 + thirtyNinePointSixPercentTaxable2017

    # Calculate 2018 and newer tax bracket
    incomeAmount2018 = incomeAmount

    # Variables for 2018 & newer tax bracket calculations
    tenPercentTaxable2018 = 0
    twelvePercentTaxable2018 = 0
    twentyTwoPercentTaxable2018 = 0
    twentyFourPercentTaxable2018 = 0
    thirtyTwoPercentTaxable2018 = 0
    thirtyFivePercentTaxable2018 = 0
    thirtySevenPercentTaxable2018 = 0

    # 10 Percent (2018)
    if (incomeAmount2018 > 9525):
        tenPercentTaxable2018 = 9525 * .1
        incomeAmount2018 = incomeAmount2018 - 9525

        # 12 Percent (2018)
        if (incomeAmount2018 > 29175) :
            twelvePercentTaxable2018 = 29175 * .12
            incomeAmount2018 = incomeAmount2018 - 29175

            # 22 Percent (2018)
            if (incomeAmount2018 > 43800):
                twentyTwoPercentTaxable2018 = 43800 * .22
                incomeAmount2018 = incomeAmount2018 - 43800

                # 24 Percent (2018)
                if (incomeAmount2018 > 75000):
                    twentyFourPercentTaxable2018 = 75000 * .24
                    incomeAmount2018 = incomeAmount2018 - 75000

                    # 32 Percent (2018)
                    if (incomeAmount2018 > 42500):
                        thirtyTwoPercentTaxable2018 = 42500 * .32
                        incomeAmount2018 = incomeAmount2018 - 42500

                        # 35 Percent (2018)
                        if (incomeAmount2018 > 300000):
                            thirtyFivePercentTaxable2018 = 300000 * .35
                            incomeAmount2018 = incomeAmount2018 - 300000

                            # 37 Percent (2018)
                            thirtySevenPercentTaxable2018 = incomeAmount2018 * .37

                        # 35%
                        else:
                            thirtyFivePercentTaxable2018 = incomeAmount2018 * .35
                    # 32%
                    else:
                        thirtyTwoPercentTaxable2018 = incomeAmount2018 * .32
                # 24%
                else:
                    twentyFourPercentTaxable2018 = incomeAmount2018 * .24
            # 22%
            else:
                twentyTwoPercentTaxable2018 = incomeAmount2018 * .22
        # 12%
        else:
            twelvePercentTaxable2018 = incomeAmount2018 * .12
    # 10%
    else:
        tenPercentTaxable2018 = incomeAmount2018 * .1      

    # Total Tax for 2018 and newer tax bracket is stored in this variable.
    totalTax2018 = tenPercentTaxable2018 + twelvePercentTaxable2018 + twentyTwoPercentTaxable2018 + twentyFourPercentTaxable2018 + thirtyTwoPercentTaxable2018 + thirtyFivePercentTaxable2018 + thirtySevenPercentTaxable2018

    # Calculate the difference
    difference = 0
    difference = totalTax2018 - totalTax2017

    # Calculate the diffrence percentage
    differencePercent = 0
    if (totalTax2017 != 0):
     differencePercent = (difference/totalTax2017) * 100

    if (differencePercent < 0):
        differencePercent = differencePercent * -1

    # Output results
    print("Income:", incomeAmount)
    print("2017 Tax:", format(totalTax2017, '.2f'))
    print("2018 Tax:", format(totalTax2018, '.2f'))
    print("Difference:", format(difference, '.2f'))
    print("Difference (Percent):", format(differencePercent, '.2f'))
    print("")

    # Prompt the user for another income value (negative value ends the loop)
    incomeAmount = int(input("Enter income as an integer with no commas: "))


## Test run #1 for Homework #2/Program Set #2
## Enter income as an integer with no commas: 8000
## Income: 8000
## 2017 Tax: 800.00
## 2018 Tax: 800.00
## Difference: 0.00
## Difference (Percent): 0.00
##
## Enter income as an integer with no commas: 15000
## Income: 15000
## 2017 Tax: 1783.75
## 2018 Tax: 1609.50
## Difference: -174.25
## Difference (Percent): 9.77
##
## Enter income as an integer with no commas: 40000
## Income: 40000
## 2017 Tax: 5738.75
## 2018 Tax: 4739.50
## Difference: -999.25
## Difference (Percent): 17.41
##
## Enter income as an integer with no commas: 100000
## Income: 100000
## 2017 Tax: 20981.75
## 2018 Tax: 18289.50
## Difference: -2692.25
## Difference (Percent): 12.83
##
## Enter income as an integer with no commas: 200000
## Income: 200000
## 2017 Tax: 49399.25
## 2018 Tax: 45689.50
## Difference: -3709.75
## Difference (Percent): 7.51
##
## Enter income as an integer with no commas: 500000
## Income: 500000
## 2017 Tax: 153818.85
## 2018 Tax: 150689.50
## Difference: -3129.35
## Difference (Percent): 2.03
##
## Enter income as an integer with no commas: 1000000
## Income: 1000000
## 2017 Tax: 351818.85
## 2018 Tax: 335689.50
## Difference: -16129.35
## Difference (Percent): 4.58
##
## Enter income as an integer with no commas: 10000000
## Income: 10000000
## 2017 Tax: 3915818.85
## 2018 Tax: 3665689.50
## Difference: -250129.35
## Difference (Percent): 6.39
##
## Enter income as an integer with no commas: -1
##
##
## Test run #2 for Homework #2/Program Set #2
## Enter income as an integer with no commas: -1
##
## 
## Test run #3 for Homework #2/Program Set #2
## Enter income as an integer with no commas: 10000
## Income: 10000
## 2017 Tax: 1033.75
## 2018 Tax: 1009.50
## Difference: -24.25
## Difference (Percent): 2.35
##
## Enter income as an integer with no commas: 28000
## Income: 28000
## 2017 Tax: 3733.75
## 2018 Tax: 3169.50
## Difference: -564.25
## Difference (Percent): 15.11
##
## Enter income as an integer with no commas: 77000
## Income: 77000
## 2017 Tax: 14988.75
## 2018 Tax: 12879.50
## Difference: -2109.25
## Difference (Percent): 14.07
##
## Enter income as an integer with no commas: 82100
## Income: 82100
## 2017 Tax: 16263.75
## 2018 Tax: 14001.50
## Difference: -2262.25
## Difference (Percent): 13.91
##
## Enter income as an integer with no commas: -1
##
##
## Test run #4 for Homework #2/Program Set #2
## Enter income as an integer with no commas: 43900
## Income: 43900
## 2017 Tax: 6713.75
## 2018 Tax: 5597.50
## Difference: -1116.25
## Difference (Percent): 16.63
##
## Enter income as an integer with no commas: 191000
## Income: 191000
## 2017 Tax: 46461.75
## 2018 Tax: 42809.50
## Difference: -3652.25
## Difference (Percent): 7.86
##
## Enter income as an integer with no commas: 321000
## Income: 321000
## 2017 Tax: 89329.25
## 2018 Tax: 88039.50
## Difference: -1289.75
## Difference (Percent): 1.44
##
## Enter income as an integer with no commas: 650000
## Income: 650000
## 2017 Tax: 213218.85
## 2018 Tax: 206189.50
## Difference: -7029.35
## Difference (Percent): 3.30
##
## Enter income as an integer with no commas: -1
##
##
## Test run #5 for Homework #2/Program Set #2
## Enter income as an integer with no commas: 16700
## Income: 16700
## 2017 Tax: 2038.75
## 2018 Tax: 1813.50
## Difference: -225.25
## Difference (Percent): 11.05
##
## Enter income as an integer with no commas: 56000
## Income: 56000
## 2017 Tax: 9738.75
## 2018 Tax: 8259.50
## Difference: -1479.25
## Difference (Percent): 15.19
##
## Enter income as an integer with no commas: 45070
## Income: 45070
## 2017 Tax: 7006.25
## 2018 Tax: 5854.90
## Difference: -1151.35
## Difference (Percent): 16.43
##
## Enter income as an integer with no commas: 890
## Income: 890
## 2017 Tax: 89.00
## 2018 Tax: 89.00
## Difference: 0.00
## Difference (Percent): 0.00
##
## Enter income as an integer with no commas: -1