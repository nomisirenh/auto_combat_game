from abc import ABC
import time
import threading
from random import randrange, choice
from src.misc.color import colors

class FighterInterface (ABC, threading.Thread):
    enemy_team: list['FighterInterface']
    ally_team: list['FighterInterface']
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
        
        self.enemy_team = None
        self.ally_team = None
        self.team_color = None
        self.lock = threading.Lock()

    def attack(self, enemy: 'FighterInterface'):
        """
        Attack an enemy
        """
        
        if enemy.is_alive() and not self.is_dead and len(self.enemy_team) != 0:
            pod = enemy.parry_or_dodge()
            if pod != False and not enemy.is_dead:
                print(f"{self} ATTACK {enemy} {colors.fgYellow}{pod} !{colors.reset}")
            else:
                
                if self.critical_attack() and not enemy.is_dead and len(self.enemy_team) != 0:
                    dam = enemy.take_damage(self, 1)
                    print(f"{self} ATTACK {enemy} {colors.fgRed}({dam} dam){colors.reset} {colors.fgYellow}CRITICAL !{colors.reset}")

                elif not enemy.is_dead and len(self.enemy_team) != 0 and not self.is_dead:
                    dam = enemy.take_damage(self, 0)
                    print(f"{self} ATTACK {enemy} {colors.fgRed}({dam} dam){colors.reset}")

                if enemy.is_dead and enemy in self.enemy_team:
                    self.enemy_team.pop(self.enemy_team.index(enemy))
                    print(f'                    {enemy} {colors.fgYellow}IS DEAD !{colors.reset}')
            

        #return True

    def critical_attack(self) -> bool:
        """
        Return true or false depending on the chance of critical
        """
        i = randrange(0,100)
        if i <= self.critical:
            return True
        else:
            return False

    def parry_or_dodge(self):
        """
        Return true or false if the fighter parry or dodge
        """
        i = randrange(0,100)
        pod = None
        if self.parry:
            if i <= self.parry:
                pod = "PARRY"
            else:
                pod = False
        elif self.dodge:
            if i <= self.dodge:
                pod = "DODGE"
            else:
                pod = False
        else:
            pod = False

        return pod

    def take_damage(self, fighter: 'FighterInterface', critical: bool):
        """
        Set heal point depending on attacker attack value and if it's a critical attack
        """
        #with self.lock:
        heal_p = self.health_point
        if critical:
            true_damage = fighter.attack_value
        else:
            true_damage = fighter.attack_value - self.defense_value

        if true_damage < 0:
            true_damage = 0

        heal_p = self.health_point - true_damage
        if heal_p <= 0:
            self.health_point = 0
            self.is_dead = True
        else:
            self.health_point = heal_p

        return true_damage

    def set_hp_max(self):
        """
        Hp to max, use for priest to heal
        """
        #with self.lock:
        self.health_point = self.max_hp

    def set_enemy_team(self, enemies):
        self.enemy_team = enemies

    def set_ally_team(self, allies):
        self.ally_team = allies

    def set_color(self, color):
        self.team_color = color

    def set_tactic(self, tactic):
        self.tactic = tactic

    def run(self) -> None:
        fighters = self.enemy_team + self.ally_team
        for f in fighters:
            while not f.is_alive():
                pass
        
        while not self.is_dead and len(self.enemy_team) != 0:
            time.sleep(int((1000 / (self.initiative)))/1000)

            if self.tactic == None:
                self.focus_random()
            else:
                self.focus_specific_class(self.tactic)

    def focus_random(self):
        if len(self.enemy_team):
            enemy = choice(self.enemy_team)

            if enemy.is_alive() and not self.is_dead:
                with enemy.lock:
                    self.attack(enemy)

    def focus_specific_class(self, focus_class):
        if self.is_class_in(focus_class, "enemy") and len(self.enemy_team):
            enemy = choice(self.enemy_team)
            while enemy._class != focus_class and len(self.enemy_team) and self.is_class_in(focus_class, "enemy"):
                enemy = choice(self.enemy_team)

            if enemy.is_alive() and not self.is_dead:
                with enemy.lock:
                    self.attack(enemy)
        else:
            self.focus_random()

    def is_class_in(self, f_class, ally_or_enemy):
        if ally_or_enemy == "enemy":
            for enemy in self.enemy_team:
                if enemy._class == f_class:
                    return True
            return False
        else:
            for ally in self.ally_team:
                if ally._class == f_class:
                    return True
            return False

    def __str__(self) -> str:
        #return f'{self.id},{self._class}, {self.name}, {self.lastname}, attaque = {self.attack_value}, defense = {self.defense_value}, health = {self.health_point}, critical = {self.critical}, initiative = {self.initiative}, parry = {self.parry}, dodge = {self.dodge}'
        if self.team_color:
            return f'{self._class}, {self.team_color}{self.name} {self.lastname}{colors.reset}, {self.health_point} hp'
        else:
            return f'{self._class}, {self.name} {self.lastname}, {self.health_point} hp'