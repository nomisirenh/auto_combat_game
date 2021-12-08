import unittest
from unittest import mock
import src.Fighter_class.Fighter
from src.Fighter_class.Fighter import FighterInterface
from src.Fighter_class.Class import *
from src.Fighter_class.Team import Team
from random import randrange

from src.game import Game

class ClassTesting(unittest.TestCase):
    def setUp(self) -> None:
        self.war_attack = randrange(70,91)
        self.war_defense_value = randrange(70, 91)
        self.war_health_point = randrange(120, 151)
        self.war_critical = randrange(5,8)
        self.war_initiative = randrange(40,61)
        self.war_parry = randrange(40,61)

        self.wiz_attack = randrange(100,151)
        self.wiz_defense_value = randrange(20, 41)
        self.wiz_health_point = randrange(60, 71)
        self.wiz_critical = randrange(5,7)
        self.wiz_initiative = randrange(75,91)

        self.rog_attack = randrange(40,61)
        self.rog_defense_value = randrange(30, 51)
        self.rog_health_point = randrange(70, 81)
        self.rog_critical = randrange(15,21)
        self.rog_initiative = randrange(75,91)
        self.rog_dodge = randrange(40,71)

        self.pri_attack = randrange(30,61)
        self.pri_defense_value  = randrange(60, 81)
        self.pri_health_point = randrange(70, 90)
        self.pri_critical = randrange(5,7)
        self.pri_initiative = randrange(50,60)
        self.pri_parry = randrange(30,51)
        
    def test_warrior(self):
        attack = randrange(70,91)
        defense_value = randrange(70, 91)
        health_point = randrange(120, 151)
        critical = randrange(5,8)
        initiative = randrange(40,61)
        parry = randrange(40,61)
        
        
        with self.assertRaises(AssertionError):
            warrior = Warrior("name", "lastname", 1000, self.war_attack, self.war_health_point, self.war_critical, self.war_initiative, self.war_parry)
        with self.assertRaises(AssertionError):
            warrior = Warrior("name", "lastname", attack, 1000, health_point, critical, initiative, parry)
        with self.assertRaises(AssertionError):
            warrior = Warrior("name", "lastname", attack, defense_value, 1000, critical, initiative, parry)
        with self.assertRaises(AssertionError):
            warrior = Warrior("name", "lastname", attack, defense_value, health_point, 1000, initiative, parry)
        with self.assertRaises(AssertionError):
            warrior = Warrior("name", "lastname", attack, defense_value, health_point, critical, 1000, parry)
        with self.assertRaises(AssertionError):
            warrior = Warrior("name", "lastname", attack, defense_value, health_point, critical, initiative, 1000)
        with self.assertRaises(AssertionError):
            warrior = Warrior("name", "lastname", attack, defense_value, health_point, critical, initiative, parry, 1000)

    def test_wizard(self):
        attack = randrange(100,151)
        defense_value = randrange(20, 41)
        health_point = randrange(60, 71)
        critical = randrange(5,7)
        initiative = randrange(75,91)
        
        with self.assertRaises(AssertionError):
            wizard = Wizard("name", "lastname", 1000, defense_value, health_point, critical, initiative,)
        with self.assertRaises(AssertionError):
            wizard = Wizard("name", "lastname", attack, 1000, health_point, critical, initiative)
        with self.assertRaises(AssertionError):
            wizard = Wizard("name", "lastname", attack, defense_value, 1000, critical, initiative)
        with self.assertRaises(AssertionError):
            wizard = Wizard("name", "lastname", attack, defense_value, health_point, 1000, initiative)
        with self.assertRaises(AssertionError):
            wizard = Wizard("name", "lastname", attack, defense_value, health_point, critical, 1000)
        with self.assertRaises(AssertionError):
            wizard = Wizard("name", "lastname", attack, defense_value, health_point, critical, initiative, 1000)
        with self.assertRaises(AssertionError):
            wizard = Wizard("name", "lastname", attack, defense_value, health_point, critical, initiative, None, 1000)

    def test_rogue(self):
        attack = randrange(40,61)
        defense_value = randrange(30, 51)
        health_point = randrange(70, 81)
        critical = randrange(15,21)
        initiative = randrange(75,91)
        dodge = randrange(40,71)
        
        with self.assertRaises(AssertionError):
            rogue = Rogue("name", "lastname", 1000, defense_value, health_point, critical, initiative, None, dodge)
        with self.assertRaises(AssertionError):
            rogue = Rogue("name", "lastname", attack, 1000, health_point, critical, initiative, None, dodge)
        with self.assertRaises(AssertionError):
            rogue = Rogue("name", "lastname", attack, defense_value, 1000, critical, initiative, None, dodge)
        with self.assertRaises(AssertionError):
            rogue = Rogue("name", "lastname", attack, defense_value, health_point, 1000, initiative, None, dodge)
        with self.assertRaises(AssertionError):
            rogue = Rogue("name", "lastname", attack, defense_value, health_point, critical, 1000, None, dodge)
        with self.assertRaises(AssertionError):
            rogue = Rogue("name", "lastname", attack, defense_value, health_point, critical, initiative, 1000, dodge)
        with self.assertRaises(AssertionError):
            rogue = Rogue("name", "lastname", attack, defense_value, health_point, critical, initiative, None, 1000)


    def test_priest(self):
        attack = randrange(30,61)
        defense_value  = randrange(60, 81)
        health_point = randrange(70, 90)
        critical = randrange(5,7)
        initiative = randrange(50,60)
        parry = randrange(30,51)
        
        with self.assertRaises(AssertionError):
            priest = Priest("name", "lastname", 1000, defense_value, health_point, critical, initiative, parry)
        with self.assertRaises(AssertionError):
            priest = Priest("name", "lastname", attack, 1000, health_point, critical, initiative, parry)
        with self.assertRaises(AssertionError):
            priest = Priest("name", "lastname", attack, defense_value, 1000, critical, initiative, parry)
        with self.assertRaises(AssertionError):
            priest = Priest("name", "lastname", attack, defense_value, health_point, 1000, initiative, parry)
        with self.assertRaises(AssertionError):
            priest = Priest("name", "lastname", attack, defense_value, health_point, critical, 1000, parry)
        with self.assertRaises(AssertionError):
            priest = Priest("name", "lastname", attack, defense_value, health_point, critical, initiative, 1000)
        with self.assertRaises(AssertionError):
            priest = Priest("name", "lastname", attack, defense_value, health_point, critical, initiative, parry, 1000)

    def test_team(self):
        warrior = Warrior("toto", "tata", self.war_attack, self.war_defense_value,self.war_health_point,self.war_critical,self.war_initiative,self.war_parry)
        priest = Priest("foo", "bar", self.pri_attack, self.pri_defense_value, self.pri_health_point,self.pri_critical,self.pri_initiative,self.pri_parry)
        wizard = Wizard("toto", "tata", self.wiz_attack, self.wiz_defense_value,self.wiz_health_point,self.wiz_critical,self.wiz_initiative)
        fighter_list = [warrior, priest]
        team  = Team(1, "red", fighter_list)

        self.assertEqual(team.get_fighters(), fighter_list)
        

    def test_attack(self):
        warrior = Warrior("toto", "tata", self.war_attack, self.war_defense_value,self.war_health_point,self.war_critical,self.war_initiative,self.war_parry)
        priest = Priest("foo", "bar", self.pri_attack, self.pri_defense_value, self.pri_health_point,self.pri_critical,self.pri_initiative,self.pri_parry)
        
        #To not parry
        src.Fighter_class.Fighter.randrange = mock.Mock()
        src.Fighter_class.Fighter.randrange.return_value = 90

        #Small life to be sure he die
        priest.is_alive = mock.Mock()
        priest.is_alive.return_value = 1
        priest.health_point = 2
        priest.defense_value = 2
        
        warrior.critical_attack = mock.Mock()
        warrior.critical_attack.return_value = 0
        warrior.enemy_team = [priest]
        warrior.attack(priest)
        self.assertTrue(priest.is_dead)

        priest.is_dead = False
        warrior.is_dead = True
        warrior.attack(priest)

        self.assertFalse(priest.is_dead)

    def test_take_damage(self):
        rogue = Rogue("toto", "tata", self.rog_attack, self.rog_defense_value,self.rog_health_point,self.rog_critical,self.rog_initiative,None,self.rog_dodge)
        warrior = Warrior("toto", "tata", self.war_attack, self.war_defense_value,self.war_health_point,self.war_critical,self.war_initiative,self.war_parry)
        priest = Priest("foo", "bar", self.pri_attack, self.pri_defense_value, self.pri_health_point,self.pri_critical,self.pri_initiative,self.pri_parry)
        wizard = Wizard("toto", "tata", self.wiz_attack, self.wiz_defense_value,self.wiz_health_point,self.wiz_critical,self.wiz_initiative)

        fighters = [rogue, warrior, priest, wizard]
        priest_test = Priest("foo", "bar", self.pri_attack, self.pri_defense_value, self.pri_health_point,self.pri_critical,self.pri_initiative,self.pri_parry)

        #test when critical_attack = 0
        for fighter in fighters:
            fighter: FighterInterface
            priest_test.attack_value = 50

            heal_p_before = fighter.health_point

            priest_test.critical_attack = mock.Mock()
            priest_test.critical_attack.return_value = 0
            fighter.take_damage(priest_test, priest_test.critical_attack())
            
            dam = priest_test.attack_value - fighter.defense_value
            if dam < 0:
                dam = 0
            #test that defense is not ignore
            #print("class: {}".format(fighter._class))
            #print("vie before: {}".format(heal_p_before))
            #print("vie : {}".format(fighter.health_point))
            #print("defense: {}".format(fighter.defense_value))
            #print("damage: {}".format(dam))
            comp = heal_p_before - dam
            self.assertEqual(fighter.health_point, comp)

            #test if defense point is bigger that the damage
            heal_p_before = fighter.health_point
            priest_test.attack_value = 20
            fighter.take_damage(priest_test, priest_test.critical_attack())
            self.assertEqual(fighter.health_point, heal_p_before)
            
            priest_test.attack_value = 1000
            fighter.take_damage(priest_test, priest_test.critical_attack())
            self.assertEqual(fighter.health_point, 0)

    def test_critical_attack(self):
        src.Fighter_class.Fighter.randrange = mock.Mock()
        src.Fighter_class.Fighter.randrange.return_value = 2

        rogue = Rogue("toto", "tata", self.rog_attack, self.rog_defense_value,self.rog_health_point,self.rog_critical,self.rog_initiative,None,self.rog_dodge)
        print(rogue.critical)
        self.assertTrue(rogue.critical_attack())

        src.Fighter_class.Fighter.randrange.return_value = 90
        self.assertFalse(rogue.critical_attack())

    def test_parry_or_dodge(self):
        src.Fighter_class.Fighter.randrange = mock.Mock()
        src.Fighter_class.Fighter.randrange.return_value = 2

        rogue = Rogue("toto", "tata", self.rog_attack, self.rog_defense_value,self.rog_health_point,self.rog_critical,self.rog_initiative,None,self.rog_dodge)
        pod = rogue.parry_or_dodge()
        self.assertEqual(pod, "DODGE")

        src.Fighter_class.Fighter.randrange.return_value = 90
        pod = rogue.parry_or_dodge()
        self.assertFalse(rogue.parry_or_dodge())

        wizard = Wizard("toto", "tata", self.wiz_attack, self.wiz_defense_value,self.wiz_health_point,self.wiz_critical,self.wiz_initiative)
        self.assertFalse(wizard.parry_or_dodge())

        warrior = Warrior("toto", "tata", self.war_attack, self.war_defense_value,self.war_health_point,self.war_critical,self.war_initiative,self.war_parry)
        self.assertFalse(warrior.parry_or_dodge())

        src.Fighter_class.Fighter.randrange.return_value = 2
        pod = warrior.parry_or_dodge()
        self.assertEqual(pod, "PARRY")

    def test_set_hp(self):
        rogue = Rogue("toto", "tata", self.rog_attack, self.rog_defense_value,self.rog_health_point,self.rog_critical,self.rog_initiative,None,self.rog_dodge)
        rogue.health_point = 20

        rogue.set_hp_max()
        self.assertEqual(rogue.health_point, rogue.max_hp)

    def test_priest_heal(self):
        #test heal
        priest = Priest("foo", "bar", self.pri_attack, self.pri_defense_value, self.pri_health_point,self.pri_critical,self.pri_initiative,self.pri_parry)
        wizard = Wizard("toto", "tata", self.wiz_attack, self.wiz_defense_value,self.wiz_health_point,self.wiz_critical,self.wiz_initiative)
        priest.enemy_team = [wizard]
        #When priest heal himself
        priest.health_point = 20
        comp = 20 + priest.defense_value//4
        priest.heal(priest)
        self.assertEqual(priest.health_point, comp)

        priest.defense_value = 1000
        priest.heal(priest)
        self.assertEqual(priest.health_point, priest.max_hp)

        #When priest heal others
        wizard.health_point = 20
        priest.heal(wizard)

        self.assertEqual(wizard.health_point, wizard.max_hp)

    def test_str(self):
        priest = Priest("foo", "bar", self.pri_attack, self.pri_defense_value, self.pri_health_point,self.pri_critical,self.pri_initiative,self.pri_parry)
        
        self.assertIn(str(priest.name), priest.__str__())
        self.assertIn(str(priest.lastname), priest.__str__())

    def test_team_alive(self):
        rogue = Rogue("toto", "tata", self.rog_attack, self.rog_defense_value,self.rog_health_point,self.rog_critical,self.rog_initiative,None,self.rog_dodge)
        warrior = Warrior("toto", "tata", self.war_attack, self.war_defense_value,self.war_health_point,self.war_critical,self.war_initiative,self.war_parry)
        priest = Priest("foo", "bar", self.pri_attack, self.pri_defense_value, self.pri_health_point,self.pri_critical,self.pri_initiative,self.pri_parry)
        wizard = Wizard("toto", "tata", self.wiz_attack, self.wiz_defense_value,self.wiz_health_point,self.wiz_critical,self.wiz_initiative)

        f = [rogue, warrior, priest, wizard]
        team = Team(1, "blue",fighters=f)

        self.assertEqual(team.fighters_alive(), 4)

    def test_set_enemy(self):
        rogue = Rogue("toto", "tata", self.rog_attack, self.rog_defense_value,self.rog_health_point,self.rog_critical,self.rog_initiative,None,self.rog_dodge)
        warrior = Warrior("toto", "tata", self.war_attack, self.war_defense_value,self.war_health_point,self.war_critical,self.war_initiative,self.war_parry)
        priest = Priest("foo", "bar", self.pri_attack, self.pri_defense_value, self.pri_health_point,self.pri_critical,self.pri_initiative,self.pri_parry)
        wizard = Wizard("toto", "tata", self.wiz_attack, self.wiz_defense_value,self.wiz_health_point,self.wiz_critical,self.wiz_initiative)

        en = [rogue, warrior, priest, wizard]

        rogue2 = Rogue("toto", "tata", self.rog_attack, self.rog_defense_value,self.rog_health_point,self.rog_critical,self.rog_initiative,None,self.rog_dodge)
        warrior2 = Warrior("toto", "tata", self.war_attack, self.war_defense_value,self.war_health_point,self.war_critical,self.war_initiative,self.war_parry)
        priest2 = Priest("foo", "bar", self.pri_attack, self.pri_defense_value, self.pri_health_point,self.pri_critical,self.pri_initiative,self.pri_parry)
        wizard2 = Wizard("toto", "tata", self.wiz_attack, self.wiz_defense_value,self.wiz_health_point,self.wiz_critical,self.wiz_initiative)

        all = [rogue2, warrior2, priest2, wizard2]

        #rogue2 = Rogue("toto", "tata", self.rog_attack, self.rog_defense_value,self.rog_health_point,self.rog_critical,self.rog_initiative,None,self.rog_dodge)

        rogue2.set_ally_team(all)
        rogue2.set_enemy_team(en)

        self.assertEqual(rogue2.enemy_team, en)
        self.assertEqual(rogue2.ally_team, all)

    def test_fighter_set_color(self):
        rogue = Rogue("toto", "tata", self.rog_attack, self.rog_defense_value,self.rog_health_point,self.rog_critical,self.rog_initiative,None,self.rog_dodge)
        rogue.set_color("\033[32m")

        self.assertEqual(rogue.team_color, "\033[32m")






