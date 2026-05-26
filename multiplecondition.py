eng = int(input("enter english marks : "))

maths = int(input("enter maths marks : "))

if eng>=80 and maths>=80:
    print("excellent")
elif eng>=80 or maths>=80:
    print("good")
else :
    print("poor")        