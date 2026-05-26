# pass by value 
def addOne (x):
    x = x+1
    print("Inside function",x)

x = 5
addOne(x)
print("Outside function",x) 

# pass by reference

def modifylist():
    list.append(4)
    print("inside function : ",list)

list = [1,2,3]
modifylist()
print("outside function : ",list)


