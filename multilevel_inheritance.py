#program for multilevel inheritance demonstration
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display_brand(self):
        print(f"Vehicle Brand: {self.brand}")

class Car(Vehicle):
    def car_type(self):
        print(f"Car Brand: {self.brand}")
class SportsCar(Car):
    def car_speed(self):
        print(f"{self.brand} is a sports car with high speed.")

vehicle = Vehicle("Toyota")
vehicle.display_brand()
car = Car("Honda")
car.display_brand()
sports_car = SportsCar("Ferrari")
sports_car.display_brand()
sports_car.car_speed()

"""
ALGORITHM:
1. Define base class Vehicle with brand attribute and display method
2. Define Car class inheriting from Vehicle
3. Define SportsCar class inheriting from Car (multilevel inheritance)
4. Each level adds specific functionality while inheriting from parent
5. Create instances and demonstrate inheritance chain

EXAMPLE OUTPUT:
Vehicle Brand: Toyota
Vehicle Brand: Honda
Vehicle Brand: Ferrari
Ferrari is a sports car with high speed.

Inheritance Hierarchy:
Vehicle (base class)
  └── Car (inherits from Vehicle)
      └── SportsCar (inherits from Car)

Time Complexity: O(1) for each method call
Space Complexity: O(1)
Demonstrates: Multilevel inheritance, method inheritance, and specialized behavior
"""
