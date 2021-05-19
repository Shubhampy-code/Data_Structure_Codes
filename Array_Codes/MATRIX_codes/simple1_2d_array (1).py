from array import*
array = [["IncomeTexNo.","Tex Amount","Name","Address","W.T.Pay or Not","Status","Category"],["998877","30000","Anuj","BBC","Pay","High","6"],["965874","45000","Akshay","BBC","Not Pay","Low","3"],["774569","90000","Piyush","Talabpura","Pay","High","7"],["665478","150000","Lucky","Bansipura","Pay","High","9"],["554789","75000","Vikas","Ramnagar","Not Pay","Low","4"]]
i=0
while i<len(array):
    j=0
    while j<len(array[i]):
        print(array[i][j],end=" ")
        j=j+1
    print()
    i=i+1
    