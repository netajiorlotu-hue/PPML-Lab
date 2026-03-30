class Father:
    
    def skill1(self):
        print("Father class method")

class Mother:
    def skill2(self):
        print("Mother class method")

class child(Father,Mother):
    def skill3(self):
        print("child class method")
obj=child()
obj.skill3()
obj.skill1()
obj.skill2()

