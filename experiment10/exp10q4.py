class parent:
    def show(self):
        print("parent class method")

class child(parent):
    def show(self):
        print("child class method")

obj=child()
obj.show()