from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        print("Dog said it can walk")
class Snake(Animal):
    def move(self):
        print("Sanke said it can slither")

Bob = Dog()
Bob.move()

DJ = Snake()
DJ.move()
