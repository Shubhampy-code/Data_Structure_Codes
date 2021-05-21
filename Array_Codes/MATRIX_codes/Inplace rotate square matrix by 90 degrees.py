"""
Inplace rotate square matrix by 90 degrees

1 2 3 4                     4 8 12 16 
5 6 7 8                     3 7 11 15
9 10 11 12                  2 6 10 14
13 14 15 16                 1 5 9  13

1 2 3 4 5                   5 10 15 20 25
6 7 8 9 10                  4 9  14 19 24
11 12 13 14 15              3 8  13 18 23
16 17 18 19 20              2 7  12 17 22
21 22 23 24 25              1 6  11 16 21 

"""
my_array = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
l=0

k=len(my_array)
while k>0 :
    j=len(my_array[l])-(l+1)
    i = 0
    while i<len(my_array):
        print(my_array[i][j], end=" ")
        i=i+1
    print()
    l=l+1
    k=k-1
