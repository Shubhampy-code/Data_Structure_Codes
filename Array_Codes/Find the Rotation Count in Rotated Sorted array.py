"""
Find the Rotation Count in Rotated Sorted array
Input : arr[] = {15, 18, 2, 3, 6, 12}
Output: 2
Explanation : Initial array must be {2, 3,
6, 12, 15, 18}. We get the given array after 
rotating the initial array twice.

Input : arr[] = {7, 9, 11, 12, 5}
Output: 4

Input: arr[] = {7, 9, 11, 12, 15};
Output: 0

"""

from array import*
my_array = array('i',[9,11,12,15,7])
count = 1
j = len(my_array)
i=0
while i < j:
    if my_array[j-1] >= my_array[0]:
        count=0
        break
    elif my_array[i]<my_array[i+1]:
        count= count+1
    else:
        break    
    i=i+1
print("number of rotation : " + str(count))
