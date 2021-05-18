#find minimun in shorted and rotated array
from array import*
my_array = array('i',[3,4,5,6,7,8,1])
#my_array = array('i',[1,2,3,4,5,6,7])


lower=0
upper = len(my_array)-1
while lower<= upper :
    mid  = int((lower+upper)/2)
    if my_array[mid] > my_array[lower]:
        lower = mid
        
    elif my_array[mid] < my_array[lower]:
        upper = mid
        
    elif mid == lower:
        index = (mid+1)
        break
    elif mid == 0:
        index = upper
        break
print("Minimum number present in array : " + str(my_array[index]))