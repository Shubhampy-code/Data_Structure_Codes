#find largest and smallest number in the array.

from array import*
my_array = array("i",[56562,2222,563,2,65555,926,347,32,659,6181,9722,4533,1244,505,7566,9577,88])
i=0
largest_num = my_array[i]
small_num = my_array[i]
while i < len(my_array):
    if my_array[i]>=largest_num:
        largest_num = my_array[i]
    elif my_array[i]<=small_num:
        small_num = my_array[i]

    i=i+1
print("largest number = " + str(largest_num))
print("smallest number = " + str(small_num))
