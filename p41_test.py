n1= eval(input())
lst=[]

for i in range(n1,0,-1):
    lst.append(i)
    print("data",i)
print()
for i in range(n1):
    print("data",lst.pop())
