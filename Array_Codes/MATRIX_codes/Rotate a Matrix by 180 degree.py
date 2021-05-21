"""Rotate a Matrix by 180 degree
    1  2  3  4               16 15 14 13 
    5  6  7  8               12 11 10 9
    9  10 11 12              8  7  6  5
    13 14 15 16              4  3  2  1  

    1  2  3  4  5            25 24 23 22 21
    6  7  8  9  10           20 19 18 17 16 
    11 12 13 14 15           15 14 13 12 11
    16 17 18 19 20           10 9  8  7  6
    21 22 23 24 25           5  4  3  2  1

"""
from array import*
my_array = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
count = 0
i = 0
x = len(my_array)-1
halfOfArray= int((len(my_array)*len(my_array[i]))/2)
while i < len(my_array) and count < halfOfArray :
    j=0
    y = len(my_array[i])-1
    while j<len(my_array[i]) and count < halfOfArray:
        my_array[i][j],my_array[x][y] = my_array[x][y],my_array[i][j]
        j=j+1
        y=y-1
        count=count+1
        #print(my_array)
    i=i+1
    x=x-1
print(my_array)
