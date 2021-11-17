#  Program to test functions a to j.
#
# Define constant variables.
ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]		    	#this is test run 1
#ONE_TEN =  [12, 20, 10, 14, 54, 16, 75, 38, 79, 103]   #this is test run 2, comment
#ONE_TEN = [1, 25, 25, 4, 5, 4, 7, 60, 9, 10]           #this is test run 3,
                                                        #run test run 1 first, then
                                                        #comment out test run 1 and 
                                                        #uncomment to run test run 2 
                                                        #and so forth for test run 3 


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

##    #c. Demonstrate replacing even elements with zero.
##    data = list(ONE_TEN)
##    replaceEven(data)           #call this function
##    print("After replacing even elements: ", data)
##
##    #d. Demonstrate replacing values with the larger of their neighbors.
##    data = list(ONE_TEN)
##    replaceNeighbors(data)      #call this function
##    print("After replacing with neighbors: ", data)
##
##    #e. Demonstrate removing the middle element.
##    data = list(ONE_TEN)
##    removeMiddle(data)          #call this function
##    print("After removing the middle element(s): ", data)
##
##    #f. Demonstrate moving even elements to the front of the list.
##    data = list(ONE_TEN)
##    evenToFront(data)           #call this function
##    print("After moving even elements: ", data)
##
##    #g. Demonstrate finding the second largest value.
##    print("The second largest value is: ", secondLargest(ONE_TEN))
##
##    #h. Demonstrate testing if the list is in increasing order.
##    print("The list is in increasing order: ", isIncreasing(ONE_TEN))
##
##    #i. Demonstrate testing if the list contains adjacent duplicates.
##    print("The list has adjacent duplicates: ", hasAdjacentDuplicate(ONE_TEN))
##
##    #j. Demonstrate testing if the list contains duplicates.
##    print("The list has duplicates: ", hasDuplicate(ONE_TEN))


#here are 2 sample functions for item a and b

def swapFirstLast(data:list)->None:	##????you decide what is being returned
    '''Swap the first and last element in a list.''' 
    #your codes
    pass     

def shiftRight(data:list)->None:	##????you decide what is being returned
    '''Shift the elements of list to the right.'''
    #your codes
    pass

##Complete the rest of the functions from items c to j
   
   
if __name__ == "__main__":
    main()


