class car():
    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name

model = car()
model.set_name("audi")
print(model.get_name())

model2 = car()
model2.set_name("volvo")
print(model2.get_name())
