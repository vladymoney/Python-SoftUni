from horse_specification.horse import Horse


class Appaloosa(Horse):
    max_speed = 120

    def __init__(self, name, speed):
        super(Appaloosa, self).__init__(name, speed)


    def train(self):
        self.speed += 2