

class Trainer:
    pokemons = list()
    def __init__(self, name):
        self.name = name

    def add_pokemon(self, pokemon: pokemons):
        self.pokemons.append(pokemon)
        return f"Caught {self.name} with health {self.h}"