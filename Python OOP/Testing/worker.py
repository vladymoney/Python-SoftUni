class Worker:
    INITIAL_MONEY = 0

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = self.INITIAL_MONEY

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy')

        self.money += self.salary

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'
