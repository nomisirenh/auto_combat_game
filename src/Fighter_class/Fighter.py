from abc import ABC, abstractmethod
import time
import threading
from random import randrange

class FighterInterface (ABC, threading.Thread):
    def __init__(self, name, lastname, attack_value, defense_value, health_point, critical, initiative, parry, dodge, _class, id):
        threading.Thread.__init__(self)
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
        
        self.max_hp = health_point
        self.is_dead = False

    def will_attack(self) -> bool:
        """
        Wait 1000ms / initiative
        """
        time.sleep(int((1000 / (self.initiative)))/1000)

        return True

    def critical_attack(self):
        i = randrange(0,100)
        if i <= self.critical:
            return True
        else:
            return False

    def parry_or_dodge(self):
        i = randrange(0,100)
        pod = None
        if self.parry:
            if i <= self.parry:
                pod = True
            else:
                pod = False
        elif self.dodge:
            if i <= self.dodge:
                pod = True
            else:
                pod = False
        else:
            pod = False

        return pod

    def take_damage(self, fighter: 'FighterInterface'):
        heal_p = self.health_point
        true_damage = fighter.attack_value - self.defense_value
        if true_damage < 0:
            true_damage = 0

        heal_p = self.health_point - true_damage
        if heal_p < 0:
            self.health_point = 0
            self.is_dead = True
        else:
            self.health_point = heal_p

    def run(self) -> None:
        #while self.is_dead is not True:
        print(self)

    def __str__(self) -> str:
        #return f'{self.id},{self._class}, {self.name}, {self.lastname}, attaque = {self.attack_value}, defense = {self.defense_value}, health = {self.health_point}, critical = {self.critical}, initiative = {self.initiative}, parry = {self.parry}, dodge = {self.dodge}'
        return f'{self.id},{self._class}, {self.name} {self.lastname}'