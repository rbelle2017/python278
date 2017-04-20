n1=n2=eval(input())

for i in range(n1):
    for j in range(n2,0,-1):
        if j>(i+1):
            print(" ",end="")
        else:            
            print("*",end="")
            if (j-1)>0:
                print("*",end="")
    print()
