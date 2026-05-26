cp = int(input("enter the cost price : "))

sp = int(input("enter the selling price : "))

# x = sp - cp 

# if x>0: 
#     print("profit")
# elif x<0:
#     print("loss")
# else :
#     print("no profit no loss")        

if cp>sp:
    print("loss")
elif sp>cp:
    print("profit")
else :
    print("no profit no loss")