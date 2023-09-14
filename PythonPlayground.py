
class Player:
    """player class"""
    def __init__(self, health=100):
        self.health = health

    def print_player(self, p):
        '''prints the satus of the player'''
        print(f"This player has {p.health} health.")

player1 = Player()
#Player().print_player(player1)

"""
    def print_player(self):
        '''prints the satus of the player'''
        print(f"This player has {self.health} health.")

player1.print_player() 
"""

class NFLteam:
    salary_cap = 198200000
    def __init__(self, city, name):
        self.city = city
        self.name = name 

    @classmethod
    def change_salary_cap(cls, new_cap):
        cls.salary_cap = new_cap

# NFLteam.change_salary_cap(2)
team1 = NFLteam("Yokohama", "PortMafia")
NFLteam.change_salary_cap(2)
print(team1.salary_cap)

team1.change_salary_cap(2)
