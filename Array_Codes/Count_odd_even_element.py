# how many odd and how many even number present in array.

from array import*
my_array = array('i',[4,5,6,7,8,9,3,3,3,3,3,3,3,1,2])
i=0
found = 0
odd=0
even = 0
while i < len(my_array):
    if ((my_array[i])%2==0):
        even = even + 1
    elif ((my_array[i])%2 != 0):
        odd = odd + 1
    i=i+1
print("Odd number present in array is : " + str(odd))
print("Even number present in array is : " + str(even))

