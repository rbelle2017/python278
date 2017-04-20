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
        print(self.avg())
        

s1=student("Tom","M")
s1.add(80)
s1.add(70)
s1.add(67)
s1.add(90)
s1.add(80)

        
