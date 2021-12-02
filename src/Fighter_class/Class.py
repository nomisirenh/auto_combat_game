from src.Fighter_class.Fighter import FighterInterface
from random import randrange

class Warrior(FighterInterface):
    def __init__(self, name, lastname, attack_value = randrange(70,91), defense_value = randrange(70, 91), health_point = randrange(120, 151)\
        , critical = randrange(5,8), initiative = randrange(40,61), parry = randrange(40,61), dodge = None, _class = "warrior", id = None):
        super().__init__(name, lastname, attack_value, defense_value, health_point, critical, initiative, parry, dodge, _class, id)

        assert attack_value <= 90 and attack_value >= 70
        assert defense_value <= 90 and defense_value >= 70
        assert health_point <= 150 and health_point >= 120
        assert critical <= 8 and critical >= 5
        assert initiative <= 60 and initiative >= 40
        assert parry <= 60 and parry >= 40
        assert dodge == None

class Rogue(FighterInterface):
    def __init__(self, name, lastname, attack_value = randrange(40,61), defense_value = randrange(30, 51), health_point = randrange(70, 81)\
        , critical = randrange(15,21), initiative = randrange(75,91), parry = None, dodge = randrange(40,71), _class = "Rogue", id = None):
        super().__init__(name, lastname, attack_value, defense_value, health_point, critical, initiative, parry, dodge, _class, id)

        assert attack_value <= 60 and attack_value >= 40
        assert defense_value <= 50 and defense_value >= 30
        assert health_point <= 80 and health_point >= 70
        assert critical <= 20 and critical >= 15
        assert initiative <= 90 and initiative >= 75
        assert parry == None
        assert dodge <= 71 and dodge >= 40

class Wizard(FighterInterface):
    def __init__(self, name, lastname, attack_value = randrange(100,151), defense_value = randrange(20, 41), health_point = randrange(60, 71)\
        , critical = randrange(5,7), initiative = randrange(75,91), parry = None, dodge = None, _class = "Wizard", id = None):
        super().__init__(name, lastname, attack_value, defense_value, health_point, critical, initiative, parry, dodge, _class, id)

        assert attack_value <= 150 and attack_value >= 100
        assert defense_value <= 40 and defense_value >= 20
        assert health_point <= 70 and health_point >= 60
        assert critical <= 7 and critical >= 5
        assert initiative <= 91 and initiative >= 75
        assert parry == None
        assert dodge == None

class Priest(FighterInterface):
    def __init__(self, name, lastname, attack_value = randrange(30,61), defense_value = randrange(60, 81), health_point = randrange(70, 90)\
        , critical = randrange(5,7), initiative = randrange(50,60), parry = randrange(30,51), dodge = None, _class = "Priest", id = None):
        super().__init__(name, lastname, attack_value, defense_value, health_point, critical, initiative, parry, dodge, _class, id)

        assert attack_value <= 60 and attack_value >= 30
        assert defense_value <= 81 and defense_value >= 60
        assert health_point <= 90 and health_point >= 70
        assert critical <= 7 and critical >= 5
        assert initiative <= 60 and initiative >= 50
        assert parry <= 50 and parry >= 30
        assert dodge == None

class Team():
    def __init__(self, id, name: str, fighters: list[FighterInterface]):
        self.id = id
        self.name = name
        self.fighters = fighters

        self.is_alive = 10

    def get_fighters(self):
        return self.fighters

    def is_in(self, fighter: FighterInterface):
        if fighter in self.fighters:
            return True

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
