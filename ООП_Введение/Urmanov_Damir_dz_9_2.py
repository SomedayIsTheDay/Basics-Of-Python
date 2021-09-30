class Road:
    def __init__(self, length=5000, width=20):
        self._length = length
        self._width = width

    def full_weight_of_asphalt(self, _weight=25, _thickness=5):
        print(f'{self._length} м * {self._width} м * {_weight} кг * {_thickness} см ='
              f' {(self._length * self._width * _weight * _thickness) / 1000:.0f}')  # or // instead of :.0f


Road().full_weight_of_asphalt()
