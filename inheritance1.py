class vehicle():
   def seating_capacity(self,fare):
       self.fare = fare
   def get_fare(self):
       return fare * 100
       
       

class bus(vehicle):
    def seating_capacity(self, fare):
        return super().seating_capacity(fare)
    def get_fare1(self):
       return ((100 * self.fare)/10)
        
    

fare = float(input("Enter the number of seats : "))
child1 = bus()
child1.seating_capacity(fare)
print(child1.get_fare())

print(child1.get_fare1()+child1.get_fare())


