'''
7 : {1,7}
10:{1,2,5,10}
'''

n=eval(input())
ct=0
for i in range(1,n+1):
    if n%i==0:
       ct+=1

if ct==2:
    print(n,"is prime")
else:
    print(n,"is not prime")
