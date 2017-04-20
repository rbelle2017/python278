n1=eval(input())
n2=n1
for i in range(n1):    
    for j in range(n2,0,-1):
        if j>(n1-i):
            print(' ',end="")
        else:
            print('*',end="")
    print()
