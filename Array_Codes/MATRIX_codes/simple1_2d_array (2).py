from array import*
array = [["Name","Address","Account no.","Balance","status"],["Anuj","BBC","123456","1000","Low"],["Akshay","BBC","124567","1100","Low"],["Piyush","Talabpura","234567","1500","High"],["lucky","Bansipura","345678","4500","Medium"],["Vikas","Ramnagar","456789","6000","High"]]
i=0
while i<len(array):
    j=0
    while j<len(array[i]):
        print(array[i][j],end=" ")
        j=j+1
    print()
    i=i+1