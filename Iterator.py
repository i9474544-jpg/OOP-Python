class PowersOfTwo:
    def __init__(self):
        self.value = 1

    def __iter__(self):
        return self

    def __next__(self):
        current = self.value
        self.value *= 2
        return current


powers = PowersOfTwo()

for _ in range(10):
    print(next(powers))
