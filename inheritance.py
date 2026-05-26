class parent():
    def __init__(self):
        self._super_attribute = True
        print("This is parent class")
class child(parent):
    def __init__(self):
        super().__init__()
        print("This is child class")
        print(self._super_attribute)
        
child1 = child()
