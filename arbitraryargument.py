# def addallnumbers(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum 


# output = addallnumbers(2,3,4,5)
# print("the sum is : ",output)

def studentinfo(**kwargs):        
    for x,y in kwargs.items():
        print(x,"is",y)

studentinfo(name ="mohit", age=20,city ="gwalior")
studentinfo(name ="prathmika", age=20,city ="pune")


