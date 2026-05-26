class numbers():
    def numb(self,n):
        self.n = n
    def square(self):
        return self.n**2
    def cube(self):
        return self.n**3

number1 = numbers()
n = int(input("Enter the number : "))
number1.numb(n)
print("The square of number is : ",number1.square())
print("The cube of the number is : ",number1.cube())
