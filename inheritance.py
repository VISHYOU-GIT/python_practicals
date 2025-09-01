#program for inheritance demonstration
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
       return f"{self.name} makes a sound."
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."



dog = Dog("Buddy")
    

print(dog.speak())

"""
ALGORITHM:
1. Define base class Animal with __init__ and speak methods
2. Define derived class Dog inheriting from Animal
3. Override speak method in Dog class to provide specific behavior
4. Create instance of Dog class
5. Call speak method (uses overridden version)

EXAMPLE OUTPUT:
Buddy barks.

OOP Concepts Demonstrated:
- Inheritance: Dog class inherits from Animal class
- Method Overriding: Dog.speak() overrides Animal.speak()
- Polymorphism: Same method name, different behavior
Time Complexity: O(1)
Space Complexity: O(1)
"""
  