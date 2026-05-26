class reactangle():
    def set_dimensions(self,height,width):
        self.height = height
        self.width = width
    def area(self):
        return self.height * self.width
    def perimeter(self):
        return (self.height + self.width)*2
    
rectangle1 = reactangle()
h = int(input("Enter the height : "))
w = int(input("Enter the width : "))

rectangle1.set_dimensions(h,w)


print("The height and widhth is : ",rectangle1.height,rectangle1.width)
print("The area of reactangle is : ",rectangle1.area())
print("The perimeter of reactangle is : ",rectangle1.perimeter())
