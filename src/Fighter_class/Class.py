from src.Fighter_class.Fighter import FighterInterface
from random import randrange

class Warrior(FighterInterface):
    def __init__(self, name, lastname, attack_value = randrange(70,91), defense_value = randrange(70, 91), health_point = randrange(120, 151)\
        , critical = randrange(5,8), initiative = randrange(40,61), parry = randrange(40,61), dodge = None, _class = "warrior", id = None):
        super().__init__(name, lastname, attack_value, defense_value, health_point, critical, initiative, parry, dodge, _class, id)

    def will_attack(self) -> bool:
        return super().will_attack()

    def take_damage(self, damage):
        return super().take_damage(damage)

class Rogue(FighterInterface):
    def __init__(self, name, lastname, attack_value = randrange(40,61), defense_value = randrange(30, 51), health_point = randrange(70, 81)\
        , critical = randrange(15,21), initiative = randrange(75,91), parry = None, dodge = randrange(40,71), _class = "Rogue", id = None):
        super().__init__(name, lastname, attack_value, defense_value, health_point, critical, initiative, parry, dodge, _class, id)

    def will_attack(self) -> bool:
        return super().will_attack()

    def take_damage(self, damage):
        return super().take_damage(damage)

class Wizard(FighterInterface):
    def __init__(self, name, lastname, attack_value = randrange(100,151), defense_value = randrange(20, 41), health_point = randrange(60, 71)\
        , critical = randrange(5,7), initiative = randrange(75,91), parry = None, dodge = None, _class = "Wizard", id = None):
        super().__init__(name, lastname, attack_value, defense_value, health_point, critical, initiative, parry, dodge, _class, id)

    def will_attack(self) -> bool:
        return super().will_attack()

    def take_damage(self, damage):
        return super().take_damage(damage)

class Priest(FighterInterface):
    def __init__(self, name, lastname, attack_value = randrange(30,61), defense_value = randrange(60, 81), health_point = randrange(70, 90)\
        , critical = randrange(5,7), initiative = randrange(50,60), parry = randrange(30,51), dodge = None, _class = "Priest", id = None):
        super().__init__(name, lastname, attack_value, defense_value, health_point, critical, initiative, parry, dodge, _class, id)

    def will_attack(self) -> bool:
        return super().will_attack()

    def take_damage(self, damage):
        return super().take_damage(damage)

class Team():
    fighters : list[FighterInterface]
    def __init__(self, id, name, fighters):
        self.id = id
        self.name = name
        self.fighters = fighters

    def get_fighters(self):
        return self.fighters

    def team_str(self):
        """
        Print all fighters that is in the team
        """
        print(f'Equipe {self.name} contient:')
        
        for fighter in self.fighters:
            print("--> ", end="")
            print(fighter)
        

if __name__ == '__main__':
    pass
