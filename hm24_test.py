n=eval(input())
ct=0
for i in range(2,n+1):
    ct=0
    for j in range(2,i):
        if i%j==0:
           ct+=1

    if ct==0:
        print(i,"is prime")

