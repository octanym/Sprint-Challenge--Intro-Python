# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    def __init__(self, name, engine):
        pass


class GroundVehicle(Vehicle):
    def __init__(self, wheels, name, engine):
        super().__init__(name, engine)
        pass


class Car(GroundVehicle):
    def __init__(self, bodystyle, doors, wheels, name, engine):
        super().__init__(wheels, name, engine)


class Motorcycle(GroundVehicle):
    def __init__(self, stroke, wheels, name, engine):
        super().__init(wheels, name, engine)
        pass


class FlightVehicle(Vehicle):
    def __init__(self, flightmethod, name, engine):
        super().__init__(name, engine)
        pass


class Airplane(FlightVehicle):
    def __init__(self, bodystyle, flightmethod, name, engine):
        super().__init__(flightmethod, name, engine)
        pass


class Starship(Vehicle):
    def __init__(self, warpdrive, name, engine):
        super().__init__(name, engine)
        pass
