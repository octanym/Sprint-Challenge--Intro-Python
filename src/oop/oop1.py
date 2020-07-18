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

class Vehicle:  # base class
    def __init__(self, name=None, engine=None):
        pass


class GroundVehicle(Vehicle):
    def __init__(self, wheels=None, name=None, engine=None):
        super().__init__(name, engine)
        pass


class Car(GroundVehicle):
    def __init__(self, bodystyle=None, doors=None, wheels=None, name=None, engine=None):
        super().__init__(wheels, name, engine)
        pass


class Motorcycle(GroundVehicle):
    def __init__(self, stroke=None, wheels=None, name=None, engine=None):
        super().__init__(wheels, name, engine)
        pass


class FlightVehicle(Vehicle):
    def __init__(self, flightmethod=None, name=None, engine=None):
        super().__init__(name, engine)
        pass


class Airplane(FlightVehicle):
    def __init__(self, dualpilot=None, bodystyle=None, flightmethod=None, name=None, engine=None):
        super().__init__(flightmethod, name, engine)
        pass


class Starship(FlightVehicle):
    def __init__(self, warpdrive=None, flightmethod=None, name=None, engine=None):
        super().__init__(flightmethod, name, engine)
        pass
