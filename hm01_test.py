import random

rnum=random.randint(1,5)
gnum=eval(input("請猜-1到5的號碼:"))

if gnum==rnum:
    print("你猜對了! 答案正是",rnum)
else:
    print("你猜錯了喔~ 其實是",rnum)
