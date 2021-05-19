#find the middle element in the given row.


def GetRowMidElement(My_array,i):
    j=len(My_array[i])
    if j%2!=0:
        j=int((j-1)/2)
        element = My_array[i][j]
        return (element)

    elif j%2 == 0:
        j = int((j/2)-1)
        element = My_array[i][j]
        return (element)

my_array1 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
ValueOfI = int(input("Enter the row : "))
myElmt = GetRowMidElement(my_array1,ValueOfI)
print("Middle Element of the selected row : "+ str(myElmt))
