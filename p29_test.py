n1=eval(input())

for i in range(1,n1+1):    
    for j in range(n1,0,-1):
        if j<=i:
            if j==1:
                print("*",end="")
            else:
                print("* ",end="")
        else:
            print(" ",end="")
    print()
