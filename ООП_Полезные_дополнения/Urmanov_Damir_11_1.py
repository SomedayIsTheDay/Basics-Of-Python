class Data:
    def __init__(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y

    @classmethod
    def int_conv(cls, data):
        d, m, y = data
        return cls(int(d), int(m), int(y))

    @staticmethod
    def valid_m_y(obj):
        if obj.day > 31 or obj.day < 1 or obj.month > 12 or obj.month < 1 or obj.year > 9999 or obj.year < 1:
            print('Неверная дата')
        else:
            return f'{obj.day} d, {obj.month} m, {obj.year} y'


dmy = ['1', 12.0, 2003.00]
f = Data.int_conv(dmy)
print(Data.valid_m_y(f))
