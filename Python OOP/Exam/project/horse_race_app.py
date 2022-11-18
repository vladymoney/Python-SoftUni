from horse_race import Horserace
from horse_specification.horse import Horse
from jockey import Jockey


class HorseRaceApp():
    def __init__(self,):
        self.horses = list()
        self.jockeys = list()
        self.horse_races = list()

    def add_horse(self, horse_type, horse_name, horse_speed):
        if horse_name in self.horses:
            raise Exception(f"Horse {horse_name} has been already added!")
        elif horse_type != "Appaloosa" or horse_type != "Thoroughbred":
            pass
        else:
            self.horses.append(horse_name)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name, age):
        if jockey_name in self.jockeys:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        else:
            self.jockeys.append(jockey_name)
            return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type):
        if race_type in self.horse_races:
            raise Exception(f"Race {race_type} has been already created!")
        else:
            self.horse_races.append(race_type)
            return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name, horse_type):
        if jockey_name not in self.jockeys:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        elif horse_type not in self.horses or Horse.is_taken is True:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        elif Horse.is_taken is False and Jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."
        else:
            Jockey.horse = not None
            return f"Jockey {jockey_name} will ride the horse {Horse.name}."



    def add_jockey_to_horse_race(self, race_type, jockey_name):
        if race_type not in self.horse_races:
            raise Exception(f"Race {race_type} could not be found!")
        elif jockey_name not in self.jockeys:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        elif jockey_name in self.jockeys and Jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        elif jockey_name in Horserace.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        if jockey_name in self.jockeys and race_type in self.horse_races and Jockey.horse is not None:
            Horserace.jockeys.append(jockey_name)
            return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type):
        if race_type not in self.horse_races:
            raise Exception(f"Race {race_type} could not be found!")
        if len(Horserace.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        else:
            return f"The winner of the {race_type} race, with a speed of {Horse.speed}km/h is {Jockey.name}! Winner's horse: {Horse.name}."







