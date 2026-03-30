def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

p = 1000 
r = 5      
t = 2      

print("Simple Interest:", simple_interest(p, r, t))