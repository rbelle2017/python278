s="A friend in need is a friend indeed."

ict=0
for i in range(len(s)):
    print("s[%2d] = %s"%(i,s[i]))
ict = s.find("friend",ict)
print(ict)
ict+=1
