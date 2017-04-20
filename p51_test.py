def factF(n=0):
    facSum=1
    for i in range(1,n+1):
        facSum*=1
    return facSum

n1 =int(input())
ans =factF(n1)
print(ans)
