def number_n_To_1(n):
    if n==0:
     return 
    print(n)
    number_n_To_1(n-1)

    
 
n = int(input("Enter n : "))
print(number_n_To_1(n))