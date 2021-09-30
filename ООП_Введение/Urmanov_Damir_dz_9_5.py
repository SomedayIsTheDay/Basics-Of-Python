class Stationery:
    def __init__(self, t):
        self.title = t

    def draw(self):
        print('Starting drawing')


class Pen(Stationery):
    def draw(self):
        print(self.title)


class Pencil(Stationery):
    def draw(self):
        print(self.title)


class Handle(Stationery):
    def draw(self):
        print(self.title)


Pen('Outlining with pen').draw()
Pencil('Now outlining with pencil').draw()
Handle('Decorating with marker').draw()
