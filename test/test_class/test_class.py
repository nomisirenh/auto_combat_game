import unittest
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
        fighter_list = [Warrior("toto", "tata"), Priest("foo", "bar")]
        team  = Team(1, "red", fighter_list)

        self.assertEqual(team.get_fighters(), fighter_list)

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

        for fighter in fighters:
            fighter: FighterInterface

            heal_p_before = fighter.health_point
            fighter.take_damage(95)
            
            dam = 95 - fighter.defense_value

            print("vie start: {}".format(heal_p_before))
            print("defense {}".format(fighter.defense_value))
            print("damage: {}".format(dam))
            print(fighter._class)

            #test that defense is not ignore
            comp = heal_p_before - dam
            if comp < 0:
                comp = 0
            self.assertEqual(fighter.health_point, comp)

            #test if defense point is bigger that the damage
            heal_p_before = fighter.health_point
            fighter.take_damage(20)
            self.assertEqual(fighter.health_point, heal_p_before)

            fighter.take_damage(1000)
            self.assertEqual(fighter.health_point, 0)
        



