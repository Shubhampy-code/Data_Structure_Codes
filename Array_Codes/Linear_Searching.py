# Linear Searching.

number = int(input("Enter the number : "))
from array import*
my_array = array('i',[2,6,7,89,4,6,1,4,5,6,77])
i=0
j=0
while i < len(my_array):
    if number == my_array[i]:
        print ("number is present in array ")
        j=1
        break
    i=i+1

if j !=1 :
    print("number is not present in array") 

