# Given  number is present in array or not.

from array import*
number = array('i',[1,2,3,4,5,6,7,8,9,6,8,9,4,3,11,2,5,8,9,6,1,4,6,2,9,6,2,6,2,3])

Number = int(input("Enter the number : "))

i=0
found = 0
while i<len(number):
    if Number == number[i]:
        print(str(Number)+" is present in arrey ")
        found = 1
        break
    i=i+1
if found ==0 :
    print(str(Number)+" is not present in arrey")
    
