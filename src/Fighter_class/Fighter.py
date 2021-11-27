from abc import ABC, abstractmethod

class FighterInterface (ABC):
    def __init__(self, name, lastname, attack_value, defense_value, health_point, critical, initiative, parry, dodge):
        self.name = name
        self.lastname = lastname
        self.attack_value = attack_value
        self.defense_value = defense_value
        self.health_point = health_point
        self.critical = critical
        self.initiative = initiative
        self.parry = parry
        self.dodge = dodge

    @abstractmethod
    def attack_maneuver(self):
        pass