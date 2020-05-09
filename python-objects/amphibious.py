from boat import Boat
from car import Car

class AmphibiousVehicle(Car, Boat):
    def __init__(self, engine, tires=[], distance_traveled=0, unit='miles', **kwargs):
        super().__init__(engine=engine, tires=tires, distance_traveled=distance_traveled, unit=unit, **kwargs)
        self.boat_type = 'motor'
    def travel(self, land_distance=0, water_distance=0):
        self.voyage(water_distance)
        self.drive(land_distance)

    def __str__(self):
        return f"<{self.__class__.__name__} {self.__dict__}"

if __name__ == "__main__":
    water_car = AmphibiousVehicle('4 cylinder')
    print(water_car)