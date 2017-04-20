import itertools
import time
t1=time.time()
lst=[0,1,2,3,4,5,6,7,8,9]


num1=eval(input())
temp=[]
for i in range(0,num1):
    num2=eval(input())
    temp.append(num2)
ans=[]    
for i in itertools.permutations(lst, 10):
    if i[0]<i[1]:
        continue
    elif (i[3]*i[7])%10 != (i[4]*i[9])%10:
        continue
    elif (i[0]*1000 + i[2]*100 + i[3]*10 + i[3] )*(i[5]*100 + i[6]*10 + i[7])==(i[1]*1000 + i[2]*100 + i[4]*10 + i[4] )*(i[5]*100 + i[8]*10 + i[9]):
        n1=i[0]*1000 + i[2]*100 + i[3]*10 + i[3]
        n2=i[5]*100 + i[6]*10 + i[7]
        n3=i[1]*1000 + i[2]*100 + i[4]*10 + i[4]
        n4=i[5]*100 + i[8]*10 + i[9]
        ans.append("%04d*%03d=%04d*%03d"%(n1,n2,n3,n4))
        
for k in temp:
    try:
        print(ans[k-1])
    except:
        print("None.")

print(time.time()-t1)
