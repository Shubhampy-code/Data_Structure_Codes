#finD the middle element of the metrix.  

import time

def GetMiddleElementOfMetrix(My_array):
    if ((len(My_array))%2)!=0:
        i = len(My_array)
        i=int((i-1)/2)
        k=len(My_array[i])
        if k%2 != 0:
            j=len(My_array[i])
            j=int((j-1)/2)
            Element = My_array[i][j]
            return(Element)

        elif len(My_array[i])%2 == 0:
            j=len(My_array[i])
            j=int((j/2)-1)
            Element = My_array[i][j]
            return(Element)

    elif ((len(My_array)%2)==0):
        i=len(My_array)
        i=int((i-1)/2)
        k=len(My_array[i])
        if k%2 != 0:
            j=len(My_array[i])
            j=int((j-1)/2)
            Element = My_array[i][j]
            return(Element)

        elif len(My_array[i])%2 == 0:
            j=len(My_array[i])
            j=int((j/2)-1)
            Element = My_array[i][j]
            return(Element)

my_array1 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
t1 = time.perf_counter()
MidElemt = GetMiddleElementOfMetrix(my_array1)
t2 = time.perf_counter()
delta = t2 - t1
print(delta)
print("Middle Element Of the metrix : " + str(MidElemt))
    
