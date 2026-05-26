class vechile():
    def __init__(self,seating_capacity):
        self.seating_capacity = seating_capacity
    def get_fare(self):
        return self.seating_capacity * 100
    
class bus (vechile):
    def __init__(self,seating_capacity):
        super().__init__(seating_capacity)
    def get_fare(self):
        vechile_fare = super().get_fare()
        maintnance = 0.1 * vechile_fare
        total_fare = maintnance + vechile_fare
        return total_fare
    
n = float(input("Enter the no. of seats : "))
vechile1 = vechile(n)
print(vechile1.get_fare())
bus1 = bus(n)
print(bus1.get_fare())

          