from baseclass import Bicycle

class Motorcycle:

    def __init__(self, gears, gear_ratio):
        self.bike = Bicycle(gears)
        self._gear_ratio = gear_ratio

    def rev_engine(self):
        return "Composed steed roars"

    def shift_gears(self, direction="up"):
        self.bike.shift_gears(direction)

    def top_speed(self):
        return self.bike.top_speed()

    def current_gear(self):
        return self.bike.current_gear()
