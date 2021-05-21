"""Find maximum value of Sum( i*arr[i]) with only rotations on given array allowed."""

from array import*
my_array = array('i',[2,4,6,8,10,12,14,16])
TimesOfRotation = int(input("Enter the number of rotation: "))
last = 0
k=0
while k<TimesOfRotation:
    i=0
    last = my_array[0]
    while i<(len(my_array)-1):
        my_array[i] = my_array[i+1]
        i=i+1

    my_array[(len(my_array)-1)] = last
    k=k+1
print(my_array)
i=0
sum = 0
while i<len(my_array):
    sum = sum + i*my_array[i]
    i=i+1
print("maximum value of Sum : " + str(sum))

    