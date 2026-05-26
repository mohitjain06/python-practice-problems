def numbers(a,b):
    if a*b<=1000:
        return a*b
    else :
        return a+b




a = int(input("Enter value of a : "))
b = int (input("Enter value of b : "))
print(numbers(a,b))