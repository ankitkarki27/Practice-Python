def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
a=int(input("Enter a number of the factorial that you want: "))
print(f"The factorial of the number {a} is {factorial(a)}")