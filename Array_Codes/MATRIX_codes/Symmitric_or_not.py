#Check givin 2d-array is symmetric or not?
from array import*
array = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8],[5,6,7,8,9]]
i=0
count = 0
while i<len(array):
    j=0
    while j<len(array[i]):
        if array[i][j] == array[j][i]:
            count = count+1
        j =j+1
    i=i+1
if count == 25:     
    print(" your matrix is symmetric")

else:
    print(" your matrix is not symmetric")