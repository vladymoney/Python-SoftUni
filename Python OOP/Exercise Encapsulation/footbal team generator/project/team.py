class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = list()

    def add_player(self, player):
        if player in self.__players:
            return f"Player {self.__name} has already joined"
        else:
            self.__players.append(player)
            return f"Player {player} joined team {self.__name}"

    def remove_player(self, player_name):
        if player_name in self.__players:
            self.__players.remove(player_name)
            return player_name
        else:
            return f"Player {player_name} not found"