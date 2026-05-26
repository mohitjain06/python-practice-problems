def power_a_of_b(a,b):
    if b==0:
        return 1
    ans = a * power_a_of_b(a,b-1) 
    return ans

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of  : "))

print(power_a_of_b(a,b))