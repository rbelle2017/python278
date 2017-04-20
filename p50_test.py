def F1(n=0):
    ans1=1
    ans2=0
    for i in range(1,n+1):
        ans1*=i
        ans2+=i
    return (ans1,ans2)

n1 = eval(input())
a,b=F1(n1)
print(a)
print(b)

        
