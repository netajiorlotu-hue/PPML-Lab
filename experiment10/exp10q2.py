class Grandparent:
    
    def property(self):
        print("grandparent class method")

class parent(Grandparent):
    def business(self):
        print("parent class method")

class child(parent):
    def education(self):
        print("child class method")
obj=child()
obj.education()
obj.business()
obj.property()

