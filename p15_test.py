sum1=0
n=0
ct=-1
maxVal=0
maxPos=0

while n!=-1:
    sum1+=n
    ct+=1
    if n>maxVal:
        maxVal=n
        maxPos=ct
    n=eval(input())

print(sum1)
print("%0.1f"%(sum1/ct))
print(maxVal)
print(maxPos)
