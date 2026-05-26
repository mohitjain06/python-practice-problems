input_strint = input("Enter the value : ")
n = int(input("Enter the n : "))

alphabets = "abcdefghijklmnopqrstuvwxyz"
reverse_alphabets = alphabets[::-1]

dict1 = dict(zip(alphabets,reverse_alphabets))
# print(dict1)
prefix = input_strint[0:n-1]
suffix = input_strint[n-1:]
mirror = ""
for i in range(0,len(suffix)):
    mirror = mirror + dict1[suffix[i]]

result = prefix + mirror 
print(result)