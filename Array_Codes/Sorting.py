from array import*
my_array = array ('i',[450,5,3,6,2,8,10,9,1,1520])

j = 0
while (j < len(my_array)):
    smallest_index = j
    i = j + 1
    while(i<len(my_array)):
        if(my_array[smallest_index] > my_array[i]):
            smallest_index = i

        i = i + 1

    temp = my_array[j]
    my_array[j] = my_array[smallest_index]
    my_array[smallest_index] = temp

    
    j = j + 1
print(my_array)

    

