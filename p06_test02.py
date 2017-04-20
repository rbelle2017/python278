n1=eval(input())
n2=eval(input())
n3=eval(input())
maxVal=0
minVal=0

if n1>n2:
    if n1>n3:
        maxVal=n1
    else:
        maxVal=n3
        minVal=n2
