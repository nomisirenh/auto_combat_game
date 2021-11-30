from abc import ABC, abstractmethod
import time

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
    def will_attack(self) -> bool:
        attack = False
        last_time = int(time.time() * 1000)
        if int(time.time() * 1000) == last_time + (1000/self.initiative):
            attack = True

        return attack

    @abstractmethod
    def take_damage(self, damage):
        true_damage = damage - self.defense_value
        if true_damage < 0:
            true_damage = 0

        self.health_point - true_damage
