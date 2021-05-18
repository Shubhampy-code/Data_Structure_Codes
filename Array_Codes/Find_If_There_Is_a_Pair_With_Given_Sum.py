""" Given a sorted and rotated array, find if there is a pair with a given sum. """

from array import*
my_array = array('i',[6,8,10,12,14,16,2,4])
Number = int(input("Enter the number : "))
i=0
while i< len(my_array):
    j=i+1
    while j<len(my_array)-1:
        if my_array[i]+my_array[j] == Number:
            print("true")
            print("There is a pair ("+str(my_array[i]) +" , "+str(my_array[j]) +" ) with sum " + str(Number))
            break
        j=j+1
    i=i+1  
