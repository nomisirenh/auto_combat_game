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
        assert health_point <= 150 and health_point >= 120
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
        assert health_point <= 80 and health_point >= 70
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
        assert health_point <= 70 and health_point >= 60
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
        assert health_point <= 90 and health_point >= 70
        assert critical <= 7 and critical >= 5
        assert initiative <= 60 and initiative >= 50
        assert parry <= 50 and parry >= 30
        assert dodge == None

    def heal(self, fighter:FighterInterface):
        #if fighter == self:
        hp = self.health_point + (self.defense_value//4)
        if hp > self.max_hp and not self.is_dead and len(self.enemy_team) != 0:
            fighter.set_hp_max()
        elif not self.is_dead and len(self.enemy_team) != 0:
            #with self.lock:
            fighter.health_point = hp
        
        if fighter == self:
            print(f'{self} {colors.fgMagenta}HEAL HIMSELF{colors.reset}')
        else:
            print(f'{self} {colors.fgMagenta}HEAL{colors.reset} {fighter}')
        #else:
            #if not self.is_dead and len(self.enemy_team) != 0 and not fighter.is_dead:
            #    fighter.set_hp_max()
            #    print(f'{self} {colors.fgMagenta}HEAL{colors.reset} {fighter}')

    def run(self) -> None:
        fighters = self.enemy_team + self.ally_team
        for f in fighters:
            while not f.is_alive():
                pass
        """for enemy in self.enemy_team:
            while enemy.is_alive() == False:
                pass

        for ally in self.ally_team:
            while ally.is_alive() == False:
                pass"""
        
        while not self.is_dead and len(self.enemy_team) != 0:
            time.sleep(int((1000 / (self.initiative)))/1000)
            i = randrange(0,2)
            if i == 0:
                if not len(self.enemy_team):
                    break
                else:
                    enemy = choice(self.enemy_team)

                if enemy.is_alive() and not self.is_dead:
                    with enemy.lock:
                        self.attack(enemy)
            else:
                if not len(self.ally_team):
                    break
                else:
                    ally = choice(self.ally_team)
                    while ally.health_point == ally.max_hp and len(self.enemy_team) != 0:
                        ally = choice(self.ally_team)

                    if ally.is_alive() and not self.is_dead:
                        with ally.lock:
                            self.heal(ally)        

if __name__ == '__main__':
    pass
