#Program for array rotation.

def ElementRotation(Dir):
    #rotation = "right"
    if Dir == "right":

        NoOfElmt = len(my_array)
        first = 0
        k=0
        while k<TimesOfRotation:
            i=(len(my_array)-1)
            first = my_array[(NoOfElmt-1)]
            while i > 0:
                my_array[i] = my_array[i-1]
                i=i-1
            my_array[0] = first
            k=k+1        
            print(my_array)   

    #rotation = "left"
    elif Dir == "left": 

        last = 0
        k=0
        while k<TimesOfRotation:
            i=0
            last = my_array[0]
            while i<(len(my_array)-1):
                my_array[i] = my_array[i+1]
                i=i+1
            my_array[(len(my_array)-1)] = last
            k=k+1
            print(my_array)


Direction = str(input("Enter the Direction Which side you want rotation : "))
from array import*
my_array = array('i',[1,2,3,4,5,6,7])
TimesOfRotation = int(input("How many element rotate : "))
ElementRotation(Direction)


