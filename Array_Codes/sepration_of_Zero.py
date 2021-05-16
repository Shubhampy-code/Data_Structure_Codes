#sepration of 0
from array import*
my_array = array('i',[1,2,0,0,5,3,0,9,9,7,0,0])

j=len(my_array)
i= 0
index = 0
while i<len(my_array)-1:
    if(my_array[i] != 0):
        my_array[i],my_array[index] = my_array[index],my_array[i]
        index = index +1
    i=i+1    

print(my_array)

