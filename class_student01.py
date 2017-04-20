class student:
    def __init__(self,name,gend):
        self.name = name
        self.gender = gend
        self.grades = []

    def avg(self):
        return sum(self.grades)/len(self.grades)

    def add(self,score):
        self.grades.append(score)

    def fcount(self):
        fct =0
        for i in range(len(self.grades)):
            if self.grades[i]<60:
                fct+=1
        return fct
    def show(self):
        print(self.name)
        print("%.2f"%(self.avg()))
        print(s1.fcount())
        
data=[]
for i in range(5):
    n1=input()
    data.append(n1)
    
s1=student(data[0],data[1])
for i in range(3):
    s1.add(int(data[i+2]))
s1.show()


        
