a = float(input("enter 1st coefficient \n"))
b = float(input("Enter second coefficient\n"))
c = float(input("Enter third coefficient\n"))
if(type(((b**2)-(4*a*c))**(0.5))!=type(1j)):
    real_r1 = (-b+((b**2)-(4*a*c))**(0.5))/(2*a)
    real_r2 = (-b-((b**2)-(4*a*c))**(0.5))/(2*a)
    print("roots are : ",real_r1,"  ",real_r2)
else:
    print("No real roots")
