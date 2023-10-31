def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n-1)
    
    
userstring = input("Number please...")
usernum = int(userstring)

print(factorial(usernum))