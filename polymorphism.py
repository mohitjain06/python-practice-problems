class Animal():
    def speaks(self):
        pass

class Dog(Animal):
    def speaks(self):
        print("barks")

class Cat(Animal):
    def speaks(self):
        print("meoww")

class Snake(Animal):
    def speaks(self):
        print("sniiss")

dog = Dog()
cat = Cat()
snake = Snake()

dog.speaks()
cat.speaks()
snake.speaks()