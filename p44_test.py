key=('P','M','H')
val=('Pikachu','Mickey Mouse','Hello kitty')
dit=dict(zip(key,val))

while True:
    n1=input()

    if n1=="-1":
        break

    if n1 in dit:
        print(dit[n1])       
    else:
        nval =input("no this data ,please enter data:")
        dit[n1]=nval
    
