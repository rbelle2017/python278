score=eval(input())
sco=0
if score >=95:
    sco=2000
elif 90<=score<=94:
    sco=1000
elif 80<=score<=89:
    sco=500
else:
    sco=0

print("獎金",sco,"元")
