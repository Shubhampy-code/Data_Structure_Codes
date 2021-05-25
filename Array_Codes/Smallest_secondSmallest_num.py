#find smallest and second smallest number in array.

from array import*
my_array = array("i",[7,71,6,0,8,7,2,1])
i=2
if my_array[0] > my_array[1]:
    small_num = my_array[1]
    scnd_num = my_array[0]
else :
    small_num = my_array[0]
    scnd_num = my_array[1]

while i < len(my_array):
    if my_array[i] < small_num :
        scnd_num = small_num
        small_num = my_array[i]
    elif my_array[i] < scnd_num:
        scnd_num = my_array[i]
         
    i=i+1

print("First smallest number : " + str (small_num))
print("second smallest number : "+ str(scnd_num))