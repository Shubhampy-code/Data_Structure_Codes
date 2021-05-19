"""
                                             1
                                             6  2
1  2  3  4  5                                11 7  3
6  7  8  9  10                               16 12 8  4
11 12 13 14 15           =======             21 17 13 9  5
16 17 18 19 20                               22 18 14 10
21 22 23 24 25                               23 19 15
                                             24 20
                                             25
                                             
"""
from array import*
array = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
k=1
a=0
while k<=len(array):
    j=0
    i=a
    while j< k and i>=0 and j<5:
        print(array[i][j],end=' ')
        i=i-1
        j=j+1
    print()
    k=k+1
    a=a+1

k=4
a=1
while k>0:
    i=4
    j=a
    count=1
    while  count<=k:
        print(array[i][j],end=' ')
        i=i-1
        j=j+1
        count = count+1
    print()
    k=k-1
    a=a+1

