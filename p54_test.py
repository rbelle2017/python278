def InputNum2List(lst):   
    while True:
        n=eval(input())
        if n==-1:
            break
        lst.append(n)
        
def Find3edMax(lst):
    lst.sort()
    print("sorted = ",lst)
    return lst[-3]

Nums=[]
InputNum2List(Nums)
print("input=",Nums)
Nums2= Nums.copy()
print("max 3rd =",Find3edMax(Nums2))
print("list =",Nums)


