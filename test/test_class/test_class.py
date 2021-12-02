import unittest
from unittest import mock
import src.Fighter_class.Fighter
from src.Fighter_class.Fighter import FighterInterface
from src.Fighter_class.Class import *
import time

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
        self.assertTrue(team.is_in(warrior))
        self.assertFalse(team.is_in(wizard))

    def test_will_attack(self):
        warrior = Warrior("toto", "tata")

        start = time.time()
        temp = warrior.will_attack()
        end = time.time()

        t = (end - start) * 1000

        self.assertEqual(int(t), int(1000/warrior.initiative))

    def test_take_damage(self):
        rogue = Rogue("toto", "tata")
        warrior = Warrior("toto", "tata")
        priest = Priest("toto", "tata")
        wizard = Wizard("toto", "tata")

        fighters = [rogue, warrior, priest, wizard]
        priest_test = Priest("titi", "tete")
        print(priest_test.attack_value)

        for fighter in fighters:
            fighter: FighterInterface
            priest_test.attack_value = 50

            heal_p_before = fighter.health_point
            fighter.take_damage(priest_test)
            
            dam = priest_test.attack_value - fighter.defense_value
            if dam < 0:
                dam = 0

            #test that defense is not ignore
            print("class: {}".format(fighter._class))
            print("vie before: {}".format(heal_p_before))
            print("vie : {}".format(fighter.health_point))
            print("defense: {}".format(fighter.defense_value))
            print("damage: {}".format(dam))
            comp = heal_p_before - dam


            self.assertEqual(fighter.health_point, comp)

            #test if defense point is bigger that the damage
            heal_p_before = fighter.health_point
            priest_test.attack_value = 20
            fighter.take_damage(priest_test)
            self.assertEqual(fighter.health_point, heal_p_before)
            
            priest_test.attack_value = 1000
            fighter.take_damage(priest_test)
            self.assertEqual(fighter.health_point, 0)

    def test_critical_attack(self):
        src.Fighter_class.Fighter.randrange = mock.Mock()
        src.Fighter_class.Fighter.randrange.return_value = 2

        rogue = Rogue("toto", "tata")
        print(rogue.critical)
        self.assertTrue(rogue.critical_attack())

        src.Fighter_class.Fighter.randrange.return_value = 90
        self.assertFalse(rogue.critical_attack())
        