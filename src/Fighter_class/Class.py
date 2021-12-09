from src.Fighter_class.Fighter import FighterInterface
from random import choice, randrange
from src.misc.color import colors
import time

class Warrior(FighterInterface):
    def __init__(self, name, lastname, attack_value, defense_value, health_point\
        , critical, initiative, parry, dodge = None, _class = "warrior", id = None):
        super().__init__(name, lastname, attack_value, defense_value, health_point, critical, initiative, parry, dodge, _class, id)

        assert attack_value <= 90 and attack_value >= 70
        assert defense_value <= 90 and defense_value >= 70
        assert health_point <= 150
        assert critical <= 8 and critical >= 5
        assert initiative <= 60 and initiative >= 40
        assert parry <= 60 and parry >= 40
        assert dodge == None

class Rogue(FighterInterface):
    def __init__(self, name, lastname, attack_value, defense_value, health_point \
        , critical, initiative, parry, dodge, _class = "Rogue", id = None):
        super().__init__(name, lastname, attack_value, defense_value, health_point, critical, initiative, parry, dodge, _class, id)

        assert attack_value <= 60 and attack_value >= 40
        assert defense_value <= 50 and defense_value >= 30
        assert health_point <= 80
        assert critical <= 20 and critical >= 15
        assert initiative <= 90 and initiative >= 75
        assert parry == None
        assert dodge <= 71 and dodge >= 40

class Wizard(FighterInterface):
    def __init__(self, name, lastname, attack_value, defense_value , health_point \
        , critical , initiative , parry = None, dodge = None, _class = "Wizard", id = None):
        super().__init__(name, lastname, attack_value, defense_value, health_point, critical, initiative, parry, dodge, _class, id)

        assert attack_value <= 150 and attack_value >= 100
        assert defense_value <= 40 and defense_value >= 20
        assert health_point <= 70
        assert critical <= 7 and critical >= 5
        assert initiative <= 91 and initiative >= 75
        assert parry == None
        assert dodge == None

class Priest(FighterInterface):
    def __init__(self, name, lastname, attack_value , defense_value, health_point \
        , critical , initiative , parry , dodge = None, _class = "Priest", id = None):
        super().__init__(name, lastname, attack_value, defense_value, health_point, critical, initiative, parry, dodge, _class, id)

        assert attack_value <= 60 and attack_value >= 30
        assert defense_value <= 81 and defense_value >= 60
        assert health_point <= 90
        assert critical <= 7 and critical >= 5
        assert initiative <= 60 and initiative >= 50
        assert parry <= 50 and parry >= 30
        assert dodge == None

    def heal(self, fighter:FighterInterface):

        hp = self.health_point + (self.defense_value//4)
        if hp > self.max_hp and not self.is_dead and len(self.enemy_team) != 0 and fighter.health_point != fighter.max_hp:
            fighter.set_hp_max()

        elif not self.is_dead and len(self.enemy_team) != 0 and fighter.health_point != fighter.max_hp:
            fighter.health_point = hp
        
        if fighter == self and not self.is_dead:
            print(f'{self} {colors.fgMagenta}HEAL HIMSELF{colors.reset}')
        elif not self.is_dead:
            print(f'{self} {colors.fgMagenta}HEAL{colors.reset} {fighter}')
    
    def set_heal_tactic(self, heal_tactic):
        self.heal_tactic = heal_tactic

    def run(self) -> None:
        fighters = self.enemy_team + self.ally_team
        for f in fighters:
            while not f.is_alive():
                pass
        
        while not self.is_dead and len(self.enemy_team) != 0:
            time.sleep(int((1000 / (self.initiative)))/1000)
            i = randrange(0,2)
            if i == 0:
                if self.tactic == None:
                    self.focus_random()
                else:
                    self.focus_specific_class(self.tactic)
            else:
                if self.heal_tactic == None:
                    self.focus_heal_random()
                else:
                    self.focus_heal_specific_class(self.heal_tactic)

    def focus_heal_random(self):
        if len(self.enemy_team):
            ally = choice(self.ally_team)
            while ally.health_point == ally.max_hp and len(self.enemy_team) != 0:
                ally = choice(self.ally_team)

            if ally.is_alive() and not self.is_dead and len(self.enemy_team) != 0:
                with ally.lock:
                    self.heal(ally)

    def focus_heal_specific_class(self, focus_class):
        if self.is_class_in(focus_class, "ally") and len(self.enemy_team):
            ally = choice(self.ally_team)
            while ally._class != focus_class and len(self.enemy_team) and self.is_class_in(focus_class, "ally"):
                ally = choice(self.ally_team)

            if ally.is_alive() and not self.is_dead:
                with ally.lock:
                    self.heal(ally)
        else:
            self.focus_random()

