class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name_and_total_income(self):
        print(f'Full name: {self.name} {self.surname}, Wage: {self._income["wage"]}, Bonus: {self._income["bonus"]},'
              f' Wage and Bonus sum: {sum(self._income.values())}')


Position('Ivan', 'Ivanov', 'Director', 15000, 6500).get_full_name_and_total_income()
