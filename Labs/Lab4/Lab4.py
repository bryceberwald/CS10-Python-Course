# Lab 4
# Question 1
# Student Name: Bryce Berwald
# Description of program: This function uses a combination of a few funcions to get the
# required solution set. The program will first call a function to create a list and then
# another function will be called to remove the even numbers from the list. Both list will
# get outputted in main.

def makeList()->list:
    '''Function creates a list to be returned'''

    # Intialize an empty list to append to.
    list = []

    # Create the list.
    for i in range(1, 11, 1):
        list.append(i)

    # Return the created list.
    return list
    

def delEven(origList : list)-> list:
    '''Function removes even numbers from a list'''

    # Remove even numbers from list.
    for item in origList:
        if(item % 2 == 0):
            origList.remove(item)

    # Return the updated list.
    return origList


def main():

    # Call function to create a list.
    originalList = makeList()

    # Print results to the console.
    print("Original List:", originalList)

    # Call function to delete even numbers from a list.
    updatedList = delEven(originalList)

    # Print updated list results to the console.
    print("List after deleting even numbers:", updatedList)
   

if __name__ == "__main__":
    main()


## Test run #1 for Question #1 (Only Test Run)
## Original List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
## List after deleting even numbers: [1, 3, 5, 7, 9]
## >>>

# Lab 4
# Question 2
# Student Name: Bryce Berwald
# Description of program: This program will create a list with value that our user will enter.
# Once 10 values have been added to our list, we will call a function in main to check for
# duplicate values and delete them from our new list if so.

def createList()->list:
    '''Function creates a list using input values to be returned'''

    # Intialize an empty list to append to.
    newList = []

    # Create the list with input values.
    for i in range(1, 11, 1):
        
        usersValue = int(input("Enter a number to be added to a list: "))
        newList.append(usersValue)

    # Return the created list.
    return newList
    

def removeDuplicates(myList : list)-> list:
    '''Function removes duplicates from a list for returning'''

    # Initialize empty list to copy content to.
    updatedList = []

    # Add items that haven't already been added once in the list.
    for item in myList:
        if (item not in updatedList):
            updatedList.append(item)

    # Return updated list.
    return updatedList


def main():

    # Call function to create a list.
    myList = createList()

    # Print original list results to the console.
    print("\nOriginal List:", myList)

    # Call function to remove duplicate values from a list.
    updatedList = removeDuplicates(myList)

    # Print list with duplicate values removed.
    print("List after removing duplicates:", updatedList)


if __name__ == "__main__":
    main()


## Test run #1 for Question #2 (Only Test Run)
## Enter a number to be added to a list: 1
## Enter a number to be added to a list: 2
## Enter a number to be added to a list: 3
## Enter a number to be added to a list: 4
## Enter a number to be added to a list: 5
## Enter a number to be added to a list: 6
## Enter a number to be added to a list: 7
## Enter a number to be added to a list: 6
## Enter a number to be added to a list: 5
## Enter a number to be added to a list: 4
##
## Original List: [1, 2, 3, 4, 5, 6, 7, 6, 5, 4]
## List after removing duplicates: [1, 2, 3, 4, 5, 6, 7]
## >>>

# Lab 4
# Question 3
# Student Name: Bryce Berwald
# Description of program: This program will take a string as input from our user and split it
# from the commas seperating the values when entered. The list will be converted to a tuple and
# passed as a parameter to create a new tuple with only postive values that will also be returned.
# Main will display both resulting tuples to the console.

def makeTuple()->tuple:
    '''Function makes a tuple from a string converted into a list'''

    # Get input values as a comma seperated list.
    inputStr= str(input("Enter the values in a tuple: "))

    # Split the input string by commas.
    inputList = inputStr.split(',')

    # Convert list to a tuple.
    inputTuple = tuple(inputList)

    # Return created tuple.
    return inputTuple
   

def makePositive(myTuple : tuple)->tuple:
    '''Function creates new tuple with positive values only'''

    # Convert tuple to list for manipulations.
    entireList = list(myTuple)

    # Initialize empty list for positive items only.
    posList = []

    # Find postive values and apend them to new list.
    for item in entireList:
        if(int(item) > 0):
            posList.append(item)

    # Convert list to tuple.
    posTuple = tuple(posList)

    # Return updated tuple.
    return posTuple


def main():
    
    # Call function to make a tuple from input string.
    newTuple = makeTuple()

    # Print the newly created tuple to the console.
    print("\nOriginal Tuple :", newTuple)

    # Call function to make a postive tuple from the previous tuple.
    positiveTuple = makePositive(newTuple)

    # Print the postive tuple that was returned by called function.
    print("New Tuple with Positive numbers :", positiveTuple)


if __name__ == "__main__":
    main()


## Test run #1 for Question #3
## Enter the values in a tuple: -10,1,2,-9,3,4,-8,5,6,-7
##
## Original Tuple : ('-10', '1', '2', '-9', '3', '4', '-8', '5', '6', '-7')
## New Tuple with Positive numbers : ('1', '2', '3', '4', '5', '6')
## >>>

# Lab 4
# Question 4
# Student Name: Bryce Berwald
# Description of program: This program will read in string values as input and append those
# values into a list. The list will be returned to examine what the largest number value in the list is.
# String values will be converted in floats for comparisons and return the largest value. With that
# information we will call our final function to display nthe resulting list in specified format with the
# largest number in list highlighted as discussed.

def readValues()->list:
    '''Function reads string input values which are appended to the returned list'''

    # Initialize empty list.
    newList = []
    
    # Give the user a display message.
    print("Please enter values, Q to quit: ")

    # Get string input value.
    inputStr = str(input())

    # Loop until user specifies so.
    while(inputStr != "Q"):
        newList.append(inputStr)
        inputStr = str(input())

    # Return the newly created list.
    return newList


def findLargest(myList : list)->float:
    '''Funtion finds largest value in list and returns value as floating point'''

    # Intialize largest value to zero.
    largestValue = 0.0

    # Loop through list contents doing float comparisons.
    for item in myList:
        if(float(item) > largestValue):
            largestValue = float(item)

    # Return the largest value found in list.
    return largestValue


def display(newStrList : list, largestVal : float)->None:
    '''Function will output list contents with largest number highlighted'''

    # Display a message for the user.
    print("\nHere are the numbers in the list ")

    # Loop through list contents.
    for item in newStrList:
        if(float(item) == largestVal):
            print(item, "<== this is the largest number")
        else:
            print(item)


def main():

    # Call function to create list full of strings.
    newStrList = readValues()

    # Call function to find largest number in list by converting.
    largestVal = findLargest(newStrList)

    # Display the resulting values with format specified in class.
    display(newStrList, largestVal)


if __name__ == "__main__":
    main()


## Test run #1 for Question #4 (Only Test Run)
## Please enter values, Q to quit: 
## 34
## 56.7
## 4
## 9
## 76.9
## 55.4
## Q
##
## Here are the numbers in the list 
## 34
## 56.7
## 4
## 9
## 76.9 <== this is the largest number
## 55.4
## >>> 

# Lab 4
# Question 5
# Student Name: Bryce Berwald
# Description of program: This program utlizies three different sets defined as discussed in class.
# We will do some operations manipulating these sets to create new sets that will get displayed to
# the console. We will create sets A-F to be shown to the user.

def main():

    # Initialize & Create sets to be used for manipulations.
    set1 = {1,2,3,4,5}
    set2 = {2,4,6,8}
    set3 = {1,5,9,13,17}

    # Initialize empty sets.
    setA = {}
    setB = {}
    setC = {}
    setD = {}
    setE = {}
    setF = {}

    # Create set A
    setA = set1 ^ set2
    print("a.", setA)

    # Create set B
    setB = set3 ^ set2 ^ set1
    print("b.", setB)

    # Create set C
    setC = (set1 | set2 | set3) - (set1 ^ set2 ^ set3)
    print("c.", setC)

    # Create set D
    generatedList = []

    for i in range(1,26,1):
        generatedList.append(i)
    generatedSet = set(generatedList)

    setD = generatedSet - set1
    print("d.", setD)

    # Create set E
    setE = generatedSet - set1 - set2 - set3
    print("e.", setE)

    # Create set F
    setF = set1 | set2 | set3 | generatedSet
    print("f.", setF)


if __name__ == "__main__":
    main()


## Test run #1 for Question #5 (Only Test Run)
## a. {1, 3, 5, 6, 8}
## b. {3, 6, 8, 9, 13, 17}
## c. {1, 2, 4, 5}
## d. {6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}
## e. {7, 10, 11, 12, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25}
## f. {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}
## >>>