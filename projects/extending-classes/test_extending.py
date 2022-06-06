from baseclass import Bicycle
import inheritance
import composition

class TestBicycle:

    def test__get_current_gear(self):
        gears = 3
        bike = Bicycle(gears)
        expected = 1
        actual = bike.current_gear()
        assert expected == actual

    def test__shift_gear_up(self):
        gears = 3
        bike = Bicycle(gears)
        bike.shift_gears("up")
        expected = 2
        actual = bike.current_gear()
        assert expected == actual

    def test__shift_gear_down(self):
        gears = 3
        bike = Bicycle(gears)
        bike._current_gear = 2
        bike.shift_gears("down")
        expected = 1
        actual = bike.current_gear()
        assert expected == actual

    def test__get_top_speed(self):
        gears = 3
        bike = Bicycle(gears)
        bike.shift_gears("up")
        expected = 4
        actual = bike.top_speed()
        assert expected == actual

class TestMotorcycleInheritance:

    def test__get_current_gear(self):
        gears = 3
        gear_ratio = 5
        motorcycle = inheritance.Motorcycle(gears, gear_ratio)
        expected = 1
        actual = motorcycle.current_gear()
        assert expected == actual

    def test__shift_gear_up(self):
        gears = 3
        gear_ratio = 5
        motorcycle = inheritance.Motorcycle(gears, gear_ratio)
        motorcycle.shift_gears("up")
        expected = 2
        actual = motorcycle.current_gear()
        assert expected == actual

    def test__shift_gear_down(self):
        gears = 3
        gear_ratio = 5
        motorcycle = inheritance.Motorcycle(gears, gear_ratio)
        motorcycle._current_gear = 2
        motorcycle.shift_gears("down")
        expected = 1
        actual = motorcycle.current_gear()
        assert expected == actual

    def test__rev_engine(self):
        gears = 3
        gear_ratio = 5
        motorcycle = inheritance.Motorcycle(gears, gear_ratio)
        expected = "Inherited steed roars"
        actual = motorcycle.rev_engine()
        assert expected == actual

    def test__get_top_speed(self):
        gears = 3
        gear_ratio = 5
        motorcycle = inheritance.Motorcycle(gears, gear_ratio)
        motorcycle._current_gear = 2
        expected = 10
        actual = motorcycle.top_speed()
        assert expected == actual

class TestMotorcycleComposition:

    def test__get_current_gear(self):
        gears = 3
        gear_ratio = 5
        motorcycle = composition.Motorcycle(gears, gear_ratio)
        expected = 1
        actual = motorcycle.current_gear()
        assert expected == actual

    def test__shift_gear_up(self):
        gears = 3
        gear_ratio = 5
        motorcycle = composition.Motorcycle(gears, gear_ratio)
        motorcycle.shift_gears("up")
        expected = 2
        actual = motorcycle.current_gear()
        assert expected == actual

    def test__shift_gear_down(self):
        gears = 3
        gear_ratio = 5
        motorcycle = composition.Motorcycle(gears, gear_ratio)
        motorcycle._current_gear = 2
        motorcycle.shift_gears("down")
        expected = 1
        actual = motorcycle.current_gear()
        assert expected == actual

    def test__rev_engine(self):
        gears = 3
        gear_ratio = 5
        motorcycle = composition.Motorcycle(gears, gear_ratio)
        expected = "Composed steed roars"
        actual = motorcycle.rev_engine()
        assert expected == actual

    def test__get_top_speed(self):
        gears = 3
        gear_ratio = 5
        motorcycle = composition.Motorcycle(gears, gear_ratio)
        motorcycle._current_gear = 2
        expected = 10
        actual = motorcycle.top_speed()
        assert expected == actual

