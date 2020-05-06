class Airplane:

    def __init__(self, make, model, year, max_speed, odometer, distance_traveled):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = odometer
        self.distance_traveled = distance_traveled
        self.is_flying = False

    def take_off(self):
        self.is_flying = True
        taking_off = f'{self.make.title()} {self.model.title()} with maximum speed of {self.max_speed} km/hour is taking off from airport.'
        return taking_off

    def fly(self):
        flying = f'The initial odometer value of {self.model.title()} was: {self.odometer} km.'
        self.odometer += self.distance_traveled
        return flying

    def land(self):
        self.is_flying = False
        landing = f'After {self.model.title()} landed, the odometer value increased to {self.odometer} km.'
        return landing

my_plane = Airplane('Boeing','X-43','2004', 11230, 0, 22460)
print(my_plane.take_off())
print(my_plane.fly())
print(my_plane.land())
