n=100

for i in range(1,n+1):
    if(i%3==0 or i%10==3 or i//10==3):
        continue
    print(i,end=' ')
