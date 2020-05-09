class Vehicle:
    """
    Vehicle is a type that describes a machine that helps us travel.
    """

    def __init__(self, distance_traveled=0, unit='miles', **kwargs):
        """
        Customizes the initialization of a Vehicle object.
        """
        self.distance_traveled = distance_traveled
        self.unit = unit

    # # To do multiple constructors in python
    # @classmethod
    # def bicycle(cls,tires=None):
    #     if not tires:
    #         tires = [cls.default_tire, cls.default_tire]
    #     return cls(None,tires)

    # @staticmethod


    # >>> bike = Vehicle.bicycle()

    def description(self):
        # dont print, return.
        return f"A {self.__class__.__name__} that has traveled {self.distance_traveled} {self.unit}."
    # Inheritance; Polymorphism; Data Hiding
