#Rotate the given no of element in the 2d matrix

from array import*
my_array = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
rotation = int(input("How many element rotate : "))
k=0
while k < rotation:

    i = 0
    I =  0
    extra = my_array[0][0]
    while i<len(my_array) :
        
        j=0
        nxt_index = j+1
        while j<len(my_array[i])   :
            nxt_index = j+1
            if j==len(my_array[i])-1 and i !=len(my_array)-1:
                I=I+1
                my_array[i][j] = my_array[I][0]
                break
            if nxt_index != len(my_array):   
                my_array[i][j] = my_array[i][nxt_index]
            elif i == len(my_array)-1 and  j == len(my_array[i])-1:
                my_array[len(my_array)-1][len(my_array[i])-1] = extra 
            j=j+1
        i=i+1
        
    print(my_array)
    k=k+1
