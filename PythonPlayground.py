'''
class Student:
    """lol """
    boob = "yes"
    def __init__(self, grade="A"):
        self.grade_ = grade
    noob = "no"

best_student = Student()
best_student.first_name = "Cossette"
best_student.last_name = "Gomez"

Student.noob = "maybe"

ok_student = Student()

print(best_student.first_name, best_student.noob)
print(ok_student.noob)
'''
'''
Cossette Gomez
<__main__.Student object at 0x00000138CE007D60>
'''

class Player:
    """Simple player class"""
    def __init__(self, pw="mushroom", health=100, score=0, level=1):
        self.health = health
        self.score = score
        self.level = level
        self.powerups = [pw]
        
    def print_player(self):
        if self.health <=0:
            print("dead lol")
        else:
           print(self.health)

    def add_powerup(self, pu):
        self.powerups.append(pu)

    def print_powerups(self):
        if len(self.powerups) ==0:
            print("you are weak sauce")
        print(self.powerups) 

def increase_level(player):
    player.level += 1
    print(f"You are at level {player.level}")


mario = Player() #the __init__ is called magically 
mario.print_player()

mario.add_powerup("mushroom")
mario.add_powerup("star")
print(mario.powerups)

peach = Player("fire flower")
peach.print_powerups() 

increase_level(peach) 