def f1():
    x=0
    print("f1()",x)

def f2():
    print("f2()",x)


def f3():
    print("f3()",x)
    global x
    x=20
    print("f3()",x)

x=10
f1()
f2()
f3()
print(x)
