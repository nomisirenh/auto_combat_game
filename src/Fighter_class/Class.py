from src.Fighter_class.Fighter import FighterInterface
from random import randrange

class Warrior(FighterInterface):
    def __init__(self, name, lastname, attack_value = randrange(70,91), defense_value = randrange(70, 91), health_point = randrange(120, 151), critical = randrange(5,8), initiative = randrange(40,61), parry = randrange(40,61), dodge = None):
        super().__init__(name, lastname, attack_value, defense_value, health_point, critical, initiative, parry, dodge)
        self._class = "warrior"

    def attack_maneuver(self):
        return super().attack_maneuver()

class Rogue(FighterInterface):
    def __init__(self, name, lastname, attack_value = randrange(40,61), defense_value = randrange(30, 51), health_point = randrange(70, 81), critical = randrange(15,21), initiative = randrange(75,91), parry = None, dodge = randrange(40,71)):
        super().__init__(name, lastname, attack_value, defense_value, health_point, critical, initiative, parry, dodge)
        self._class = "Rogue"

    def attack_maneuver(self):
        return super().attack_maneuver()

class Wizard(FighterInterface):
    def __init__(self, name, lastname, attack_value = randrange(100,151), defense_value = randrange(20, 41), health_point = randrange(60, 71), critical = randrange(5,7), initiative = randrange(75,91), parry = None, dodge = None):
        super().__init__(name, lastname, attack_value, defense_value, health_point, critical, initiative, parry, dodge)
        self._class = "Wizard"

    def attack_maneuver(self):
        return super().attack_maneuver()

class Priest(FighterInterface):
    def __init__(self, name, lastname, attack_value = randrange(30,61), defense_value = randrange(60, 81), health_point = randrange(70, 90), critical = randrange(5,7), initiative = randrange(50,60), parry = randrange(30,51), dodge = None):
        super().__init__(name, lastname, attack_value, defense_value, health_point, critical, initiative, parry, dodge)
        self._class = "Priest"

    def attack_maneuver(self):
        return super().attack_maneuver()


    