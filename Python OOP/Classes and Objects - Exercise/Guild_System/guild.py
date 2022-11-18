from player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = list()

    def assign_player(self, player):
        if player in self.players:
            return f"Player {player} is already in the guild."
        elif player.guild != self.name:
            return f"Player {player.name} is in another guild."
        else:
            self.players.append(player)
            return f"Welcome player {player} to the guild {self.name}"

    def kick_player(self, player_name):
        if player_name not in self.players:
            return f"Player {player_name} is not in the guild."
        else:
            self.players.remove(player_name)
            return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for player in self.players:
            result += player.player_info() + '\n'
        return result.strip()


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())



