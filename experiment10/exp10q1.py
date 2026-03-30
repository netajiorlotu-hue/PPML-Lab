class parent:
    def __init__(self,a):
        self.a=a
    def method(self):
        print("parent class method")

class child(parent):
    obj=parent(10)
    obj.method()
