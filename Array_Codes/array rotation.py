no_of_rotation = int(input("How many times you want to rotate : "))
from array import*
my_array = array('i',[1,2,3,4,5,6,7])
j=0
while j<no_of_rotation:
    i=0
    k=1
    extra = my_array[0]
    while i<len(my_array) and k<len(my_array):
        my_array[i] = my_array[k]
        i=i+1
        k=k+1
    my_array[len(my_array)-1] = extra

    j=j+1
    print(my_array)


    
