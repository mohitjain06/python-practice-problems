class reactangle():
    def __init__(self,height,width):
        self.height = height
        self.width = width
        print(f"the height of reactamgle is : {height} and width is : {width}")

    def set_dimensions(self,height,width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return (self.height + self.width)*2
    
rectangle1 = reactangle(3,4)
rectangle2 = reactangle(5,6)
rectangle3 = reactangle(3,8)

print(f"The area of reactangle1 is : {rectangle1.area()} and area of reactangle2 is : {rectangle2.area()} and area of reactangle3 is : {rectangle3.area()}")

print(f"The perimeter of reactangle1 is : {rectangle1.perimeter()} and perimeter of reactangle2 is : {rectangle2.perimeter()} and perimeter of reactangle3 is : {rectangle3.perimeter()}")
