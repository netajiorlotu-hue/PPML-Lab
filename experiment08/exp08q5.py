def PrimeOrNot(n):
    if n==1:
        print("1 is special case")
        return
    if n>1:
        for i in range(2,n):
            if(n%i==0):
                print("not prime")
                return
        else:
            print("prime number")      

PrimeOrNot(int(input("Enter a number")))         
