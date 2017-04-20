n1=eval(input())
n2=n1
for i in range(n1):    
    for j in range(n2):
        if j<(n1-(i+1)):
            print(' ',end="")
        else:
            print('*',end="")
    print()
