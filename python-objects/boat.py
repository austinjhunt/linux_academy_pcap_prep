from vehicle import Vehicle

class Boat(Vehicle):

    def __init__(self, boat_type='sail', distance_traveled=0, unit='miles', **kwargs):
        super().__init__(distance_traveled=distance_traveled, unit=unit, **kwargs)
        self.boat_type = boat_type

    def voyage(self, distance):
        self.distance_traveled += distance

    def description(self):
        init = super().description()
        return f"{init} using a {self.boat_type}"
if __name__ == "__main__":
    boat = Boat()

    print(boat.description())