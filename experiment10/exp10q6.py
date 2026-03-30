class parent:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return parent(self.a+other.a)
    def display(self):
        print("sum",self.a)

p1=parent(10)
p2=parent(20)
p3=parent(30)

p4=p1+p2+p3
p4.display()