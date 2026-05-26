def fibonnai(n):
     if n==1:
        return 0
     elif n==2:
        return 1
     else:
         return (fibonnai(n-1) + fibonnai(n-2))
     
n = int(input("enter n : "))
for i in range(1,n+1):
  print(fibonnai(i))