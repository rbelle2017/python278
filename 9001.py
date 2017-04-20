import time
t1=time.time()
nLst=[0,1,2,3,4,5,6,7,8,9]
s="大小絃嘈切如急雨私語"
ans=[]
def chkEqual(lst):   
    n1_0= lst[0]*1000 + lst[2]*100 + lst[3]*10 +lst[3]
    n1_1= lst[5]*100 + lst[6]*10 + lst[7]    
 
    n2_0= lst[1]*1000 + lst[2]*100 + lst[4]*10 + lst[4]
    n2_1= lst[5]*100 + lst[8]*10 + lst[9]
 
    if n1_0*n1_1== n2_0*n2_1 :
        ans.append("%04d*%03d=%04d*%03d"%(n1_0,n1_1,n2_0,n2_1))
 
 
def permutations2(n1, n2, nLst , ansNum):
    n=len(nLst)
    indices = nLst
    if ( (indices[1]*indices[5])%10 == ( indices[2]*indices[7] )%10 ):
        chkEqual([n1]+[n2]+indices)
    while True:       
        low_index = n-1
        while low_index > 0 and indices[low_index-1] > indices[low_index]:
            low_index -= 1
        if low_index == 0:
            break
        low_index -= 1
        high_index = low_index+1
        while high_index < n and indices[high_index] > indices[low_index]:
            high_index += 1
        high_index -= 1
        indices[low_index], indices[high_index] = indices[high_index], indices[low_index]
        indices[low_index+1:] = reversed(indices[low_index+1:])
 
        if ( (indices[1] * indices[5])%10 != ( indices[2] * indices[7] )%10 ):
            continue
        else:
            chkEqual([n1]+[n2]+indices)
            if(len(ans)>=ansNum):
                break
 
num1=eval(input())
temp=[]
for i in range(0,num1):
    num2=eval(input())
    temp.append(num2)
 
for i in range(1,10):   
    lst1=nLst.copy()
    lst1.pop(i)
    for j in lst1:
        if j< i:
            lst2 = lst1.copy()
            lst2.pop(j)
            permutations2(i,j,lst2,temp[-1])
        else:
            continue
 
for k in temp:
    try:
        print(ans[k-1])
    except:
        print("None.")

print(time.time()-t1)
