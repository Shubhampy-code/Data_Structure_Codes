"""
                                            ae 
                                            be ad 
aa ab ac ad ae                              ce bd ac
ba bb bc bd be                              de cd bc ab
ca cb cc cd ce       ==========>            ee dd cc bb aa
da db dc dd de                              ed dc cb ba
ea eb ec ed ee                              ec db ca
                                            eb da
                                            ea



"""

from array import*
array=[["aa","ab","ac","ad","ae"],["ba","bb","bc","bd","be"],["ca","cb","cc","cd","ce"],["da","db","dc","dd","de"],["ea","eb","ec","ed","ee"]]
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
