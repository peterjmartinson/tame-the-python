
class Bicycle:
    _gear_ratio = 2
    _current_gear = 1

    def __init__(self, gears):
        self.gears = gears

    def _shift_gears_up(self):
        if self._current_gear < self.gears:
            self._current_gear += 1
        else:
            raise ValueError("Already reached maximum gear")

    def _shift_gears_down(self):
        if self._current_gear >= 2:
            self._current_gear -= 1
        else:
            raise ValueError("Already reached minimum gear")

    def shift_gears(self, direction="up"):
        if direction == "up":
            self._shift_gears_up()
        elif direction == "down":
            self._shift_gears_down()
        else:
            raise ValueError('Please pass "up" or "down"')

    def top_speed(self):
        return self._current_gear * self._gear_ratio

    def current_gear(self):
        return self._current_gear


