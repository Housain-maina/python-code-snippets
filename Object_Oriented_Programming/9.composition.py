
class PreviousTeams:

    def __init__(self, teams=0):
        self.teams = teams

    def get_number(self):
        return self.teams


class Player:
    """
    the Player class creates an object of the PreviousTeams class when during it's when it gets instantiated,
    therefore deleting the Player class instance will also delete the PreviousTeams class it instantiated.
    """
    def __init__(self, name, previous_teams=0):
        self.name = name
        self.previous_teams = PreviousTeams(previous_teams)

    def number_of_previous(self):
        return self.previous_teams.get_number()


player = Player("Ronaldo", 4)
print(player.number_of_previous())
