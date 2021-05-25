# delete the duplicate elements
from array import*
my_array = array('i',[1,2,3,3,2,4,4,1,1,1,1,1,2,2,2,2,2,5,6,6])
i=0
#j=1
while i<len(my_array):
    j = i +1
    while  j< len(my_array):
        if my_array[i] == my_array[j]:
            my_array.pop(j)

            print(my_array)
            j = j-1
        j=j+1
    i=i+1

        