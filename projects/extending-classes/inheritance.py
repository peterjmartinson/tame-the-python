from baseclass import Bicycle

class Motorcycle(Bicycle):

    def __init__(self, gears, gear_ratio):
        super().__init__(gears)
        self._gear_ratio = gear_ratio

    def rev_engine(self):
        return "Inherited steed roars"
