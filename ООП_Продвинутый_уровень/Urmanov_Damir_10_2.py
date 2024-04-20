from abc import abstractmethod, ABC


class Clothing(ABC):
    def __init__(self, s_n_h):
        self.s_n_h = s_n_h

    @abstractmethod
    def sewing(self):
        pass


class Coat(Clothing):
    @property
    def sewing(self):
        return round(self.s_n_h / 6.5 + 0.5)


class Costume(Clothing):
    @property
    def sewing(self):
        return round(2*self.s_n_h + 0.3)


coat = Coat(200)
costume = Costume(15)
print(coat.sewing)
print(costume.sewing)
print(coat.sewing + costume.sewing)
