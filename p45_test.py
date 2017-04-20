pb = {'1':" Wor", 2.2:"gic", "Three":"rd", 4:" Ma", "Six":"ld.", 5:"A"}

s1="5-4-2.2-'1'-Six"
for i in s1.split("-"):
    if i in pb:
        print(pb[i],end="")
    elif eval(i) in pb:
        print(pb[eval(i)],end="")
