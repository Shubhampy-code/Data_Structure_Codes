#Insertion Shorting.

from array import*
my_array = array('i',[33,44,33,55,22,11])
i=0
j=1
while j <len(my_array):
    if my_array[j]<= my_array[i]:
        extra = my_array[j]
        k=0
        while k<j:
            my_array[j-k] = my_array[j-(k+1)]
            k=k+1
        my_array[0] = extra
    j=j+1
    print(my_array)
            
