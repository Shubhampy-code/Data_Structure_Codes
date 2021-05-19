#find the middle element in the given row.

def GetColMidElement(My_array,j):
    i=len(My_array)
    if i%2 !=0:
        i=int((i-1)/2)
        element = My_array[i][j]
        return (element)
    elif i%2 == 0:
        i=int((i/2)-1)
        element = My_array[i][j]
        return (element)

my_array1=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
ValueOfJ = int(input("Enter the colomn : "))
myelmt = GetColMidElement(my_array1,ValueOfJ)
print("Middle element of the given column : "+ str(myelmt))