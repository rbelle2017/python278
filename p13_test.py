n1=eval(input())
sum1=0
for i in range(1,n1+1):
    if i!=n1:
        print(i,end="+")
    else:
        print(i,end=" = ")
    sum1+=i
print(sum1)
