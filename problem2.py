word = input("Enter : ")
print("ORiginal STring : ",word)

x = list(word)

for i in x[0::2]:
    print(i)