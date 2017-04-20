n1= int(input())
cnt=0
for i in range(2,n1):
    cnt=0
    for j in range(2,i):
        if i%j==0:
            cnt+=1
    if cnt==0:
        print(i,"is prime")
