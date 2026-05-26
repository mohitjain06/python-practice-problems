class Dad():
  
    def sings(self):
        print("Dad sings well")

class Mom():
   
    def codes(self):
        print("Mom codes well")

class child(Dad,Mom):
  
    def plays(self):
        print("Child plays well")

child1 = child()
dad1 = Dad()
mom1 = Mom()

child1.plays()
dad1.sings()
mom1.codes()