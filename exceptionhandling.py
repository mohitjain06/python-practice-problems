a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))

try:
    result = a/b
except  ZeroDivisionError:
    result = None
    print("Error: cannot be divide")
finally:
    print("The division is : ",result)


