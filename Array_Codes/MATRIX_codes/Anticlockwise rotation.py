"""
Anticlockwise rotation 
1  2  3  4  5        5 10 15 20 25      00 01 02 03 04        04 14 24 34 44
6  7  8  9  10       4  9 14 19 24      10 11 12 13 14        03 13 23 33 43
11 12 13 14 15       3  8 13 18 23      20 21 22 23 24        02 12 22 32 42
16 17 18 19 20       2  7 12 17 22      30 31 32 33 34        01 11 21 31 41
21 22 23 24 25       1  6 11 16 21      40 41 42 43 44        00 10 20 30 40
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
        my_array[i][j] = my_array[j][n-i]
        my_array[j][n-i] = my_array[n-i][n-j]
        my_array[n-i][n-j] = my_array[n-j][i]
        my_array[n-j][i] = temp
        print(my_array)
        j=j+1

    print()
    i=i+1
    m=m-1