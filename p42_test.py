lst=[]
while True:
    n1=eval(input())    
    if n1==-1:
        break
    lst.append(n1)
lst.sort()
print(lst)
lst.insert(3,10)
print(lst)
print(lst.count(10))
lst.sort()
lst.reverse()
print(lst)
