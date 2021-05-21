#Separate 0,1,2
from array import*
my_array = array('i',[1,0,2,2,0,0,1,2,1,0,0,1,1,2,2,1,1,1,1,0,2,1])

i=0
count_zero =0 
count_one = 0
count_two = 0
while i<len(my_array):
    if my_array[i]==0:
        count_zero = count_zero+1
    elif my_array[i] ==2:
        count_two= count_two+1
    elif my_array[i] == 1:
        count_one = count_one+1
    i=i+1
#print(count_zero)
#print(count_one)
#print(count_two)

i=0
while i < count_zero:
    my_array[i]=0
    i=i+1
#print(my_array)

while count_one > 0:  
    my_array[i]=1
    count_one =count_one-1
    i=i+1
#print(my_array)

while count_two > 0 :
    my_array[i] = 2
    count_two =count_two-1
    i=i+1
print(my_array)