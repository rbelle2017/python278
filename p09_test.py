n1=eval(input())
n2=eval(input())
n3=eval(input())

temp=0
if n1 > n2:
    if n1> n3:
        temp=n1
    else:
        temp=n3
else:
    if n2>n3:
        temp=n2
    else:
        temp=n3

print(temp)
