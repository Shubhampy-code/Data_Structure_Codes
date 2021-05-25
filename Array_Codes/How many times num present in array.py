#Given number is how many time present in array.

from array import*
my_number = array('i',[4,5,6,7,8,9,3,3,3,3,3,3,3,1,2])
Number = int(input("Enter the number to check how many times given number is present in array :"))
i=0
found = 0
count=0
while i<len(my_number):
    if my_number[i] == Number:
        count=count+1
        found = 1     
    i=i+1

if found == 0:
    print(str(Number)+" is not present in array ")

if found ==1:
    print(str(Number)+ " present in arrey " + str(count)+" times")
