from abc import ABC, abstractmethod
import time

class FighterInterface (ABC):
    def __init__(self, name, lastname, attack_value, defense_value, health_point, critical, initiative, parry, dodge, _class, id):
        self.name = name
        self.lastname = lastname
        self.attack_value = attack_value
        self.defense_value = defense_value
        self.health_point = health_point
        self.critical = critical
        self.initiative = initiative
        self.parry = parry
        self.dodge = dodge
        self._class = _class
        self.id = id

    @abstractmethod
    def will_attack(self) -> bool:

        time.sleep((1000 / (self.initiative))/1000)

        return True

    @abstractmethod
    def take_damage(self, damage):
        true_damage = damage - self.defense_value
        if true_damage < 0:
            true_damage = 0

        self.health_point - true_damage

    def __str__(self) -> str:
        #return f'{self.id},{self._class}, {self.name}, {self.lastname}, attaque = {self.attack_value}, defense = {self.defense_value}, health = {self.health_point}, critical = {self.critical}, initiative = {self.initiative}, parry = {self.parry}, dodge = {self.dodge}'
        return f'{self.id},{self._class}, {self.name} {self.lastname}'