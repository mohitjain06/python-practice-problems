n = int(input("Enter the size of list : "))

list = []
for i in range(n):
   num = int(input())
   list.append(num)



indx1 = int(input("Enter indx1 : "))
indx2 = int(input("Enter indx2 : "))

temp = list[indx1]
list[indx1]= list[indx2]
list[indx2] = temp
print(list)