# Homework 3
# Program Set 1
# Student Name: Bryce Berwald
# Student ID#: 1212962
# Program Description: This program will use a comination of a few different functions to help
# us manipulate lists. The manipulations done will be returned to main for outputting the new
# lists resulting values. Three constant lists will be used for our test cases to ensure that all
# functions are working properly. The original list will be display first, that way you can see
# the different operations that have been done to these lists.

# Define constant variables.
ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]		    	#this is test run 1
#ONE_TEN =  [12, 20, 10, 14, 54, 16, 75, 38, 79, 103]   #this is test run 2
#ONE_TEN = [1, 25, 25, 4, 5, 4, 7, 60, 9, 10]           #this is test run 3

# Function for Part A.
def swapFirstLast(data:list)->list:	
    '''Swap the first and last element in a list.''' 

    # Create variables to hold the first and last values in the list.
    first = data[0]
    last = data[len(data)-1]

    # Replace the first and last values.
    data[0] = last
    data[len(data)-1] = first

    # Return the updated list.
    return data


# Function for Part B.
def shiftRight(data:list)->list:
    '''Shift the elements of list to the right.'''
    
    # Insert the last element of the list to the front.
    data.insert(0, data[len(data)-1])

    # Reverse list to remove last element.
    data.reverse()
    data.remove(data[0])

    # Reverse list back to original order.
    data.reverse()

    # Return updated list.
    return data


# Function for Part C.
def replaceEven(data : list)->list:
    '''Function replaces even elements with a value of zero.'''

    # Initialize an empty list to be used.
    replacedList = []

    # Loop through creating a new list with zeros replacing even numbers.
    for item in data:
        if (item % 2 == 0):
            replacedList.append(0)
        else:
            replacedList.append(item)

    # Return updated list.
    return replacedList


# Function for Part D.
def replaceNeighbors(data : list)->list:
    '''Function replaces neighbors with larger values.'''

    # Loop through replacing neighbor values as needed.
    for index in range(1, len(data)-1, 1):
        if data[index-1] < data[index+1]:
            data[index] = data[index+1]
        else:
            data[index] = data[index-1]

    # Return updated list.
    return data
            

# Function for Part E.
def removeMiddle(data : list)->list:
    '''Function removes middle element or element(s) for odd length lists.'''

    # Find half of the length of list.
    half = len(data) / 2

    # Convert float to integer (possible truncation)
    half = int(half)

    # Length of list is an even number.
    if (len(data) % 2 == 0):
        data.remove(data[half])
        half = len(data) / 2
        half = int(half)
        data.remove(data[half])
    # Length of list is an odd number.
    else:
        data.remove(data[half])

    # Return updated list.
    return data


# Function for Part F.
def evenToFront(data : list)->list:
    '''Function moves all even numbers to the front of the list.'''

    # Initialize an empty list to be used.
    newList = []

    # Loop through list appending even numbers to new list.
    for i in range(0, len(data), 1):
        if (data[i] % 2 == 0):
            newList.append(data[i])

    # Loop through list appending odd numbers to end of new list.
    for i in range(0, len(data), 1):
        if (data[i] % 2 != 0):
            newList.append(data[i])

    # Return updated list.
    return newList


# Function for Part G.
def secondLargest(data :list)->int:
    '''Function finds the second largest value in list.'''

    # Initialize variable that contains largest value of the list.
    largestValue = 0

    # Find largest value in list.
    for index in range(0, len(data), 1):
        if(data[index] > largestValue):
            largestValue = data[index]

    # Remove the largest value in list.
    data.remove(largestValue)
    
    # Reset the largest value variable.
    largestValue = 0

    # Finding the second largest value in the list. (largest value already removed)
    for index in range(0, len(data), 1):
        if(data[index] > largestValue):
            largestValue = data[index]

    # Return the second largest value for the list.
    return largestValue


# Function for Part H.
def isIncreasing(data : list)->bool:
    '''Function determines if list is in increasing order.'''

    # Initialize an empty list to be used.
    sortedList = []

    # Loop through copying list contents to new list.
    for item in data:
        sortedList.append(item)

    # Sort the newly created list.
    sortedList.sort()

    # Compare the original list to the sorted list.
    if (data != sortedList):
        return False
    else:
        return True


# Function for Part I.
def hasAdjacentDuplicate(data : list)->bool:
    '''Function determines if list has adjacent duplicates next to each other.'''

    # Loop through checking left and right values of each index.
    for index in range(1, len(data)-1, 1):
        if (data[index] == data[index+1]) or (data[index] == data[index-1]):
            return True
        else:
            return False


# Function for Part J.
def hasDuplicate(data : list)->bool:
    '''Function determines if there are multiple values in the same list.'''

    # Intialize an empty list to be used.
    sortedList = []

    # Loop through list copying contents to new list.
    for item in data:
        sortedList.append(item)

    # Sort newly created list so duplicates are next to each other.
    sortedList.sort()

    # Loop through the sorted list checking if multiple instances occur.
    for index in range(1, len(sortedList)-1, 1):
        if (sortedList[index] == sortedList[index+1]) or (sortedList[index] == sortedList[index-1]):
            return True
        else:
            return False


def main() :
    print("The original data for all functions is: ", ONE_TEN)

    #a. Demonstrate swapping the first and last element.
    data = list(ONE_TEN)
    swapFirstLast(data)         #call this function      
    print("After swapping first and last: ", data)

    #b. Demonstrate shifting to the right.
    data = list(ONE_TEN)
    shiftRight(data)            #call this function
    print("After shifting right: ", data)

    #c. Demonstrate replacing even elements with zero.
    data = list(ONE_TEN)
    replaceEven(data)           #call this function
    print("After replacing even elements: ", data)

    #d. Demonstrate replacing values with the larger of their neighbors.
    data = list(ONE_TEN)
    replaceNeighbors(data)      #call this function
    print("After replacing with neighbors: ", data)

    #e. Demonstrate removing the middle element.
    data = list(ONE_TEN)
    removeMiddle(data)          #call this function
    print("After removing the middle element(s): ", data)

    #f. Demonstrate moving even elements to the front of the list.
    data = list(ONE_TEN)
    evenToFront(data)           #call this function
    print("After moving even elements: ", data)

    #g. Demonstrate finding the second largest value.
    print("The second largest value is: ", secondLargest(ONE_TEN))

    #h. Demonstrate testing if the list is in increasing order.
    print("The list is in increasing order: ", isIncreasing(ONE_TEN))

    #i. Demonstrate testing if the list contains adjacent duplicates.
    print("The list has adjacent duplicates: ", hasAdjacentDuplicate(ONE_TEN))

    #j. Demonstrate testing if the list contains duplicates.
    print("The list has duplicates: ", hasDuplicate(ONE_TEN))
   
   
if __name__ == "__main__":
    main()


## Test run #1 for Homework #4/Program Set #1
## The original data for all functions is:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
## After swapping first and last:  [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]
## After shifting right:  [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
## After replacing even elements:  [1, 0, 3, 0, 5, 0, 7, 0, 9, 0]
## After replacing with neighbors:  [1, 3, 4, 5, 6, 7, 8, 9, 10, 10]
## After removing the middle element(s):  [1, 2, 3, 4, 7, 8, 9, 10]
## After moving even elements:  [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
## The second largest value is:  9
## The list is in increasing order:  True
## The list has adjacent duplicates:  False
## The list has duplicates:  False
## >>>
##
##
## Test run #2 for Homework #4/Program Set #1
## The original data for all functions is:  [12, 20, 10, 14, 54, 16, 75, 38, 79, 103]
## After swapping first and last:  [103, 20, 10, 14, 54, 16, 75, 38, 79, 12]
## After shifting right:  [103, 12, 20, 10, 14, 54, 16, 75, 38, 79]
## After replacing even elements:  [0, 0, 0, 0, 0, 0, 75, 0, 79, 103]
## After replacing with neighbors:  [12, 12, 14, 54, 54, 75, 75, 79, 103, 103]
## After removing the middle element(s):  [12, 20, 10, 14, 75, 38, 79, 103]
## After moving even elements:  [12, 20, 10, 14, 54, 16, 38, 75, 79, 103]
## The second largest value is:  79
## The list is in increasing order:  False
## The list has adjacent duplicates:  False
## The list has duplicates:  False
## >>> 
##
##
## Test run #3 for Homework #4/Program Set #1
## The original data for all functions is:  [1, 25, 25, 4, 5, 4, 7, 60, 9, 10]
## After swapping first and last:  [10, 25, 25, 4, 5, 4, 7, 60, 9, 1]
## After shifting right:  [10, 1, 25, 25, 4, 5, 4, 7, 60, 9]
## After replacing even elements:  [1, 25, 25, 0, 5, 0, 7, 0, 9, 0]
## After replacing with neighbors:  [1, 25, 25, 25, 25, 25, 60, 60, 60, 10]
## After removing the middle element(s):  [1, 25, 25, 5, 7, 60, 9, 10]
## After moving even elements:  [4, 4, 60, 10, 1, 25, 25, 5, 7, 9]
## The second largest value is:  25
## The list is in increasing order:  False
## The list has adjacent duplicates:  True
## The list has duplicates:  True
## >>> 