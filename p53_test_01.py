def factF(n=0):
    facSum=1
    for i in range(1,n+1):
        facSum*=i
    return facSum

def P(n,m):
    return (factF(n)/factF(n-m))

def C(n,m):
    return P(n,m)/factF(m)

x = int(input())
y = int(input())
ans =C(x,y)
print(int(ans))
