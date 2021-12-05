import unittest
from unittest import mock
import src.Fighter_class.Fighter
from src.Fighter_class.Fighter import FighterInterface
from src.Fighter_class.Class import *
from src.Fighter_class.Team import Team
import time

from src.game import Game

class ClassTesting(unittest.TestCase):
    def test_warrior(self):
        warrior = Warrior("toto","tata")
        
        with self.assertRaises(AssertionError):
            warrior = Warrior(name = "toto", lastname="tata", attack_value=1000)
        with self.assertRaises(AssertionError):
            warrior = Warrior(name = "toto", lastname="tata", defense_value=1000)
        with self.assertRaises(AssertionError):
            warrior = Warrior(name = "toto", lastname="tata", health_point=1000)
        with self.assertRaises(AssertionError):
            warrior = Warrior(name = "toto", lastname="tata", critical=1000)
        with self.assertRaises(AssertionError):
            warrior = Warrior(name = "toto", lastname="tata", initiative=1000)
        with self.assertRaises(AssertionError):
            warrior = Warrior(name = "toto", lastname="tata", parry=1000)
        with self.assertRaises(AssertionError):
            warrior = Warrior(name = "toto", lastname="tata", dodge=1000)

    def test_wizard(self):
        wizard = Wizard("toto","tata")
        
        with self.assertRaises(AssertionError):
            wizard = Wizard(name = "toto", lastname="tata", attack_value=1000)
        with self.assertRaises(AssertionError):
            wizard = Wizard(name = "toto", lastname="tata", defense_value=1000)
        with self.assertRaises(AssertionError):
            wizard = Wizard(name = "toto", lastname="tata", health_point=1000)
        with self.assertRaises(AssertionError):
            wizard = Wizard(name = "toto", lastname="tata", critical=1000)
        with self.assertRaises(AssertionError):
            wizard = Wizard(name = "toto", lastname="tata", initiative=1000)
        with self.assertRaises(AssertionError):
            wizard = Wizard(name = "toto", lastname="tata", parry=1000)
        with self.assertRaises(AssertionError):
            wizard = Wizard(name = "toto", lastname="tata", dodge=1000)

    def test_rogue(self):
        rogue = Rogue("toto","tata")
        
        with self.assertRaises(AssertionError):
            rogue = Rogue(name = "toto", lastname="tata", attack_value=1000)
        with self.assertRaises(AssertionError):
            rogue = Rogue(name = "toto", lastname="tata", defense_value=1000)
        with self.assertRaises(AssertionError):
            rogue = Rogue(name = "toto", lastname="tata", health_point=1000)
        with self.assertRaises(AssertionError):
            rogue = Rogue(name = "toto", lastname="tata", critical=1000)
        with self.assertRaises(AssertionError):
            rogue = Rogue(name = "toto", lastname="tata", initiative=1000)
        with self.assertRaises(AssertionError):
            rogue = Rogue(name = "toto", lastname="tata", parry=1000)
        with self.assertRaises(AssertionError):
            rogue = Rogue(name = "toto", lastname="tata", dodge=1000)

    def test_priest(self):
        priest = Priest("toto","tata")
        
        with self.assertRaises(AssertionError):
            priest = Priest(name = "toto", lastname="tata", attack_value=1000)
        with self.assertRaises(AssertionError):
            priest = Priest(name = "toto", lastname="tata", defense_value=1000)
        with self.assertRaises(AssertionError):
            priest = Priest(name = "toto", lastname="tata", health_point=1000)
        with self.assertRaises(AssertionError):
            priest = Priest(name = "toto", lastname="tata", critical=1000)
        with self.assertRaises(AssertionError):
            priest = Priest(name = "toto", lastname="tata", initiative=1000)
        with self.assertRaises(AssertionError):
            priest = Priest(name = "toto", lastname="tata", parry=1000)
        with self.assertRaises(AssertionError):
            priest = Priest(name = "toto", lastname="tata", dodge=1000)

    def test_team(self):
        warrior = Warrior("toto", "tata")
        priest = Priest("foo", "bar")
        wizard = Wizard("toto", "tata")
        fighter_list = [warrior, priest]
        team  = Team(1, "red", fighter_list)

        self.assertEqual(team.get_fighters(), fighter_list)
        

    def test_attack(self):
        warrior = Warrior("toto", "tata")
        priest = Priest("foo", "bar")
        
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
        rogue = Rogue("toto", "tata")
        warrior = Warrior("toto", "tata")
        priest = Priest("toto", "tata")
        wizard = Wizard("toto", "tata")

        fighters = [rogue, warrior, priest, wizard]
        priest_test = Priest("titi", "tete")

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

        rogue = Rogue("toto", "tata")
        print(rogue.critical)
        self.assertTrue(rogue.critical_attack())

        src.Fighter_class.Fighter.randrange.return_value = 90
        self.assertFalse(rogue.critical_attack())

    def test_parry_or_dodge(self):
        src.Fighter_class.Fighter.randrange = mock.Mock()
        src.Fighter_class.Fighter.randrange.return_value = 2

        rogue = Rogue("toto", "tata")
        pod = rogue.parry_or_dodge()
        self.assertEqual(pod, "DODGE")

        src.Fighter_class.Fighter.randrange.return_value = 90
        pod = rogue.parry_or_dodge()
        self.assertFalse(rogue.parry_or_dodge())

        wizard = Wizard("toto", "tata")
        self.assertFalse(wizard.parry_or_dodge())

        warrior = Warrior("toto", "tata")
        self.assertFalse(warrior.parry_or_dodge())

        src.Fighter_class.Fighter.randrange.return_value = 2
        pod = warrior.parry_or_dodge()
        self.assertEqual(pod, "PARRY")

    def test_set_hp(self):
        rogue = Rogue("toto", "tata")
        rogue.health_point = 20

        rogue.set_hp_max()
        self.assertEqual(rogue.health_point, rogue.max_hp)

    def test_priest_heal(self):
        #test heal
        priest = Priest("toto", "tata")
        wizard = Wizard("toto", "tata")

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
        priest = Priest("toto", "tata")
        
        self.assertIn(str(priest.name), priest.__str__())
        self.assertIn(str(priest.lastname), priest.__str__())

    def test_team_alive(self):
        rogue = Rogue("toto", "tata")
        warrior = Warrior("toto", "tata")
        priest = Priest("toto", "tata")
        wizard = Wizard("toto", "tata")

        f = [rogue, warrior, priest, wizard]
        team = Team(1, "blue",fighters=f)

        self.assertEqual(team.fighters_alive(), 4)

    def test_set_enemy(self):
        rogue = Rogue("toto", "tata")
        warrior = Warrior("toto", "tata")
        priest = Priest("toto", "tata")
        wizard = Wizard("toto", "tata")

        en = [rogue, warrior, priest, wizard]

        rogue2 = Rogue("toto", "tata")
        warrior2 = Warrior("toto", "tata")
        priest2 = Priest("toto", "tata")
        wizard2 = Wizard("toto", "tata")

        all = [rogue2, warrior2, priest2, wizard2]

        rogue2 = Rogue("toto", "tata")

        rogue2.set_ally_team(all)
        rogue2.set_enemy_team(en)

        self.assertEqual(rogue2.enemy_team, en)
        self.assertEqual(rogue2.ally_team, all)

    def test_fighter_set_color(self):
        rogue = Rogue("toto", "tata")
        rogue.set_color("\033[32m")

        self.assertEqual(rogue.team_color, "\033[32m")






