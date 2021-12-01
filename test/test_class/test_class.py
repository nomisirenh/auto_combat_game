import unittest
from src.Fighter_class.Fighter import FighterInterface
from src.Fighter_class.Class import *
from random import randrange

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
        fighter_list = [Warrior("toto", "tata"), Priest("foo", "bar")]
        team  = Team(1, "red", fighter_list)

        self.assertEqual(team.get_fighters(), fighter_list)
