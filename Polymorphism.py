# Base Class: Vehicle

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement this method")


# Subclasses with Polymorphism

class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road"


class Plane(Vehicle):
    def move(self):
        return "✈️ Flying in the sky"


class Boat(Vehicle):
    def move(self):
        return "⛵ Sailing on the water"


class Bicycle(Vehicle):
    def move(self):
        return "🚴 Pedaling along the path"


# Program Execution / Testing

if __name__ == "__main__":
    # Create a list of vehicles
    vehicles = [Car(), Plane(), Boat(), Bicycle()]

    # Polymorphic behavior: all call move(), but behave differently
    for v in vehicles:
        print(v.move())
