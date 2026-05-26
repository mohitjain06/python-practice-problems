def sumOneToN(n):
    sum = 0
    for i in range(1 , n+1):
        sum +=i
    return sum 

n = int(input("Enter n : "))
output = sumOneToN(n)
print("The sum of all till n is :",output)    

    