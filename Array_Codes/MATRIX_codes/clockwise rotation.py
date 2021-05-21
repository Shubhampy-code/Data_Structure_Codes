"""
clockwise rotation
1  2  3  4  5        21 16 11 6 1      00 01 02 03 04        40 30 20 10 00
6  7  8  9  10       22 17 12 7 2      10 11 12 13 14        41 31 21 11 01
11 12 13 14 15       23 18 13 8 3      20 21 22 23 24        42 32 22 12 02 
16 17 18 19 20       24 19 14 9 4      30 31 32 33 34        43 33 23 13 03
21 22 23 24 25       25 20 15 10 5     40 41 42 43 44        44 34 24 14 04
"""
from array import*
my_array = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
temp = 0
i=0
n = len(my_array)-1
m = n
while i<=m :
    j=i
    while j<m:
        
        temp = my_array[i][j]        
        my_array[i][j] = my_array[n-j][i]
        my_array[n-j][i] = my_array[n-i][n-j]
        my_array[n-i][n-j] = my_array[j][n-i]
        my_array[j][n-i] = temp
        
        print(my_array)
        j=j+1

    print()
    i=i+1
    m=m-1