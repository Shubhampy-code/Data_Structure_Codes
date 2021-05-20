#bubble Sorting

from array import*
my_array = array('i',[9,8,945,7,6,5,4,3,2,1,0,562])

h=(len(my_array)-1)
while h>=0:
    j=1
    i=0
    while i<len(my_array) and j<len(my_array):
        if my_array[i] > my_array[j]:
            temp = my_array[j]
            my_array[j] = my_array[i]
            my_array[i] = temp
        i=i+1
        j=j+1
        
    h=h-1
    print(my_array)