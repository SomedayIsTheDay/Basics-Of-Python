import random


class Car:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def car_name(self):
        print(f'{self.name}:')

    def go(self):
        print(f'{self.name} is going ', '\n')

    def stop(self):
        print(f'{self.name} stopped', '\n')

    def turn_to(self, direction=('left', 'right')):
        print(f'{self.name} turned {random.choice(direction)}', '\n')

    def show_speed(self):
        print(f'Speed at the moment: {self.speed}', '\n')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Speed at the moment: {self.speed}. You have exceeded the speed limit. Slow down.', '\n')
        else:
            super().show_speed()


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Speed at the moment: {self.speed}. You have exceeded the speed limit.', '\n')
        else:
            super().show_speed()


class SportCar(Car):  # ?????????
    pass


class PoliceCar(Car):
    def chasing(self):
        if sport_car.speed > 120:
            print(f'{self.name} is chasing {sport_car.name} now', '\n')


town_car = TownCar('Kia', 'Red', 90, False)
work_car = WorkCar('Lada', 'Gray', 30, False)
sport_car = SportCar('Lamborghini', 'Orange', 180, False)
police_car = PoliceCar('Chevrolet', 'Black', 120, True)

cars = [town_car, work_car, sport_car, police_car]

for i in cars:
    i.car_name()
    i.go()
    i.stop()
    i.show_speed()
    i.turn_to()
police_car.chasing()
