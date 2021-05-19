"""                                 
                                    5
                                    10 4
1  2  3  4  5                       15 9  3
6  7  8  9  10                      20 14 8  2
11 12 13 14 15      ===========     25 19 13 7 1  
16 17 18 19 20                      24 18 12 6
21 22 23 24 25                      23 17 11
                                    22 16 
                                    21
"""
from array import*
array=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
k=1
a=0
while k<=len(array):
    i=a
    j=4
    count = 1
    while count <=k:
        print(array[i][j],end=' ')
        j=j-1
        i=i-1
        count=count+1
    print()
    k=k+1
    a=a+1

k=4
a=3
while k>0:
    j=a
    i=4
    count = 0
    while count<k:
        print(array[i][j],end=' ')
        i=i-1
        j=j-1
        count=count+1
    print()
    k=k-1
    a=a-1
