def count_digits(n):
    if n==0:
        return 0
    else:
        return 1+count_digits(n//10)
num = int(input("Enter number:"))
print("number of digit: ",count_digits(num))