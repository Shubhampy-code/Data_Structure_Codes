# Binary Search 

from array import*
my_array = array('i',[0,11,12,13,14,15,16,17,18,19,20,21,22])
number = int(input("Enter the number to find that number is present in array or not : "))

lower = 0
upper = len(my_array)-1
while lower<= upper :
    mid  = int((lower+upper)/2)
    if my_array[mid] ==number :
        print(str(my_array[mid])+" present in array")
        break
    elif my_array[mid]< number:
        lower = mid+1
    elif my_array[mid] >number:
        upper = upper-1
