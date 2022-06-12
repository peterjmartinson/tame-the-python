class StandardIterable:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self._current_value = start

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_value >= self.end:
            raise StopIteration()
        value = self._current_value
        self._current_value += 1
        return value



class ContainerIterable:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        value = self.start
        while value < self.end:
            yield value
            value += 1
    
