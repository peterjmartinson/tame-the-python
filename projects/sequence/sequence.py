class Sequence:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self._range = self._create_range()

    def _create_range(self):
        values = []
        value = self.start
        while value < self.end:
            values.append(value)
            value += 1
        return values

    def __getitem__(self, value_index):
        return self._range[value_index]

    def __len__(self):
        return len(self._range)
