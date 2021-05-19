"""
1  2  3  4  5  6  7       ---------------->                                      1 2 3 4 5 6 7
8  9  10 11 12 13 14      ^ ------------>  !                                     14 21 28 35 42 49
15 16 17 18 19 20 21      ! ^  - - - - > ! !                                     48 47 46 45 44 43 
22 23 24 25 26 27 28      ! !  ^ --->  ! ! !             ======>                 36 29 22 15 8
29 30 31 32 33 34 35      ! !  < ----  V ! !                                     9 10 11 12 13 
36 37 38 39 40 41 42      ! < -----------v !                                     20 27 34 41
43 44 45 46 47 48 49      !<---------------v                                     40 39 38 37
                                                                                 30 23 16
                                                                                 17 18 19
                                                                                 26 33
                                                                                 32 31
                                                                                 24 25
"""
from array import*
my_array = [[1,2,3,4,5,6,7],[8,9,10,11,12,13,14],[15,16,17,18,19,20,21],[22,23,24,25,26,27,28],[29,30,31,32,33,34,35],[36,37,38,39,40,41,42],[43,44,45,46,47,48,49]]
count = 1
k = 0
c = 0
a = 0
e=1
l=0
x=1
y=2
v=0
t=2
s=0
while count<=len(my_array)*len(my_array):
    d=0
    b=c
    while d<len(my_array[a])+k and count<=len(my_array)*len(my_array):
        print(my_array[a][b],end=" ")
        b = b+1 
        d=d+1 
        count = count+1
    if count<=len(my_array)*len(my_array):
        print()
    k=k-2
    a=a+1
    c=c+1

    
    i=e
    j=len(my_array[i])-e
    while i<len(my_array)+l and count<=len(my_array)*len(my_array):
        print(my_array[i][j],end=" ")
        count=count+1
        i=i+1
    if count<=len(my_array)*len(my_array):
        print() 
    e=e+1
    l=l-1
    
    i=len(my_array)-x
    j=len(my_array)-y
    while j>=v and count<=len(my_array)*len(my_array):
        print(my_array[i][j],end=" ")
        j=j-1
        count=count+1
        
    if count<=len(my_array)*len(my_array):
        print()
    x=x+1
    y=y+1
    v=v+1


    i=len(my_array)-t
    j=s
    while i > s and count<=len(my_array)*len(my_array):
        print(my_array[i][j],end=" ")
        i=i-1
        count = count+1
    if count<=len(my_array)*len(my_array):
        print()
    t=t+1
    s=s+1