def sum_n_To_1(n):
  
    if n==1:
     return 1
    ans = n + sum_n_To_1(n-1)
    return ans


n = int(input("Enter n : "))
print(sum_n_To_1(n))