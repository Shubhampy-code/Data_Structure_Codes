from array import*
my_array = array('i',[2,6,2,5,1,8,7,3,9])

k=0
while k < len(my_array)-1:
    i=0
    j=i+1
    while i < len(my_array) and j<len(my_array):

        if my_array[j] < my_array[i]:
            extra = my_array[j]
            my_array[j] = my_array[i]
            my_array[i] = extra
        j=j+1
        i=i+1
    print(my_array)
    k=k+1
    #print(my_array)
