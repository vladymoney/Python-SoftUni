from horse_specification.horse import Horse


class Thoroughbred(Horse):
    max_speed = 140

    def __init__(self, name, speed):
        super(Thoroughbred, self).__init__(name, speed)

    def train(self):
        self.speed += 3