# Addition of rows , columns and Diagonal are same or not.
from array import*
array = [[1,2,3,4,5],[2,1,1,1,10],[1,3,5,7,9],[2,4,6,8,10],[1,4,7,2,8]]
i=0
check = 0
while i<len(array):
    j=0
    additionOfRow = 0
    while j<len(array[i]):
        additionOfRow = additionOfRow + array[i][j]
        j=j+1
    if check == additionOfRow or check ==0:
        check = additionOfRow
    else:
        print("Row " +str(i+1) + " addition is : "+str(additionOfRow))
        print("value is not same")
        break
        
    i=i+1
    print("Row " +str(i) + " addition is : "+str(additionOfRow))

i=0
check = 0
while i<len(array):
    j=0
    additionOfCol = 0
    while j<len(array[i]):
        additionOfCol = additionOfCol + array[j][i]
        j=j+1
    if check == additionOfCol or check ==0:
        check = additionOfCol
    else:
        print("Col " +str(i+1) + " addition is : "+str(additionOfCol))
        print("value is not same")
        break    
    i=i+1
    print("Col " +str(i) + " addition is : "+str(additionOfCol))

i = 0
dia = 0
while i<len(array):
    dia = dia + array[i][i]
    i=i+1
print("Addition of diagonal : " + str(dia))

i=0
j=4
scndDia = 0
while i<len(array) and j>0:
    scndDia = scndDia+array[i][j]
    i=i+1
    j=j-1
print("Addition of diagonal : " + str(scndDia))

if scndDia ==dia:
    print("Diagnol is same ")
else :
    print("Diagnol is not same ")