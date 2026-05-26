def factorial(n):
    ans = 1 
    if n==0:
        return 1
    ans = n * factorial(n-1)
    return ans

n = int(input("Enter the number : "))

print(factorial(n))